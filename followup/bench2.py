"""Train one model with NegativeBinomialLikelihood on a real count series and record per-epoch train/val loss.

Run with PYTHONPATH pointing at the darts tree to test (master or the PR branch):
    PYTHONPATH=existing python bench.py <dataset> <model> <seed> <lr> <out.json>
"""

import json
import logging
import os
import platform
import subprocess
import sys
import tempfile
import time
import traceback
import warnings

import numpy as np
import torch

warnings.filterwarnings("ignore")
logging.disable(logging.WARNING)
torch.set_num_threads(1)  # many runs share the machine; one thread each keeps runs comparable

import darts  # noqa: E402
import pandas  # noqa: E402
import pytorch_lightning  # noqa: E402
from darts.datasets import AirPassengersDataset, TaxiNewYorkDataset, UberTLCDataset  # noqa: E402
from darts.models import RNNModel, TFTModel, TiDEModel  # noqa: E402
from darts.utils.likelihood_models import NegativeBinomialLikelihood  # noqa: E402
from pytorch_lightning.callbacks import Callback  # noqa: E402

# Raw output where softplus(x) == float32 eps, the PR's floor: log(expm1(eps)), about -15.94.
FLOOR_X = float(np.log(np.expm1(np.float64(np.finfo(np.float32).eps))))
VARIANT = os.environ.get("BENCH_VARIANT", "")

if VARIANT == "logmu":
    # Alternative fix: keep the mean in log space with no floor, so its gradient survives; floor only alpha.
    def _params_logmu(self, out):
        x = out[:, :, :, 0]
        # log(softplus(x)) equals x to float32 precision below -20; the clamp keeps the unused branch finite
        log_mu = torch.where(x < -20, x, torch.log(self.softplus(x.clamp_min(-20))))
        alpha = self.softplus(out[:, :, :, 1]).clamp_min(torch.finfo(out.dtype).eps)
        return log_mu, alpha

    def _r_logits_logmu(log_mu, alpha):
        return 1.0 / alpha, log_mu + torch.log(alpha)

    NegativeBinomialLikelihood._params_from_output = _params_logmu
    NegativeBinomialLikelihood._get_r_and_logits_from_mu_and_alpha = staticmethod(_r_logits_logmu)
elif VARIANT:
    raise ValueError(VARIANT)

# Counts of raw mean / dispersion outputs below FLOOR_X, read without touching the computation.
MODE = {"name": "train"}
STATS = {}


def _reset():
    STATS.clear()
    STATS.update(n=0, mu_below=0, alpha_below=0, nan=0, mu_min=float("inf"), alpha_min=float("inf"))


_reset()
_orig_params = NegativeBinomialLikelihood._params_from_output


def _params_recorded(self, out):
    if (MODE["name"] == "train" and torch.is_grad_enabled()) or MODE["name"] == "predict":
        with torch.no_grad():
            x = out.detach()
            xm, xa = x[:, :, :, 0], x[:, :, :, 1]
            STATS["n"] += xm.numel()
            STATS["mu_below"] += int((xm < FLOOR_X).sum())
            STATS["alpha_below"] += int((xa < FLOOR_X).sum())
            STATS["nan"] += int(torch.isnan(x).sum())
            if xm.numel() and not torch.isnan(xm).all():
                STATS["mu_min"] = min(STATS["mu_min"], float(torch.nan_to_num(xm, nan=float("inf")).min()))
                STATS["alpha_min"] = min(STATS["alpha_min"], float(torch.nan_to_num(xa, nan=float("inf")).min()))
    return _orig_params(self, out)


NegativeBinomialLikelihood._params_from_output = _params_recorded


def uber_212():
    s = UberTLCDataset(sample_freq="hourly").load()["212"]
    return s, int(np.isnan(s.values()).sum())


# name -> (loader returning (series, missing values set to 0), input_chunk_length, output_chunk_length, n_epochs)
DATASETS = {
    "air_passengers": (lambda: (AirPassengersDataset().load(), 0), 12, 6, 200),
    "taxi_new_york": (lambda: (TaxiNewYorkDataset().load(), 0), 96, 48, 30),
    "uber_tlc_212": (uber_212, 48, 24, 30),
}


def build(model, icl, ocl, epochs, seed, lr, work_dir, callback):
    common = dict(
        likelihood=NegativeBinomialLikelihood(),
        n_epochs=epochs,
        batch_size=32,
        optimizer_kwargs={"lr": lr},
        random_state=seed,
        work_dir=work_dir,
        pl_trainer_kwargs={
            "accelerator": "cpu",
            "enable_progress_bar": False,
            "enable_model_summary": False,
            "logger": False,
            "callbacks": [callback],
        },
    )
    if model == "TiDE":
        return TiDEModel(input_chunk_length=icl, output_chunk_length=ocl, **common)
    if model == "TFT":
        return TFTModel(input_chunk_length=icl, output_chunk_length=ocl, add_relative_index=True, **common)
    if model == "LSTM":
        return RNNModel(model="LSTM", input_chunk_length=icl, training_length=icl + ocl, **common)
    raise ValueError(model)


class Recorder(Callback):
    """Train loss as the batch-size-weighted mean over each epoch (darts logs only the last batch's value),
    val loss as darts logs it (the mean over the validation set), and where training was when it stopped."""

    def __init__(self):
        self.train, self.val = [], []
        self.epoch, self.batch = 0, None
        self._sum, self._n = 0.0, 0
        self.raw = []

    def on_train_epoch_start(self, trainer, pl_module):
        self.epoch, self._sum, self._n = trainer.current_epoch + 1, 0.0, 0
        _reset()

    def on_train_batch_start(self, trainer, pl_module, batch, batch_idx):
        self.batch = batch_idx + 1

    def on_train_batch_end(self, trainer, pl_module, outputs, batch, batch_idx):
        loss = outputs["loss"] if isinstance(outputs, dict) else outputs
        n = batch.past_target.shape[0]
        self._sum += float(loss) * n
        self._n += n

    def on_validation_epoch_end(self, trainer, pl_module):
        if not trainer.sanity_checking:
            self.val.append(float(trainer.callback_metrics["val_loss"]))

    def on_train_epoch_end(self, trainer, pl_module):
        self.train.append(self._sum / self._n)
        self.raw.append(dict(STATS))


def environment():
    tree = os.path.dirname(os.path.dirname(darts.__file__))
    try:
        cpu = subprocess.run(["sysctl", "-n", "machdep.cpu.brand_string"], capture_output=True, text=True).stdout.strip()
    except OSError:
        cpu = platform.processor()
    return dict(
        darts_file=darts.__file__,
        darts_commit=open(os.path.join(tree, "COMMIT")).read().strip(),
        python=platform.python_version(), torch=torch.__version__, lightning=pytorch_lightning.__version__,
        numpy=np.__version__, pandas=pandas.__version__, platform=platform.platform(), cpu=cpu,
    )


def main(dataset, model, seed, lr, out):
    load, icl, ocl, epochs = DATASETS[dataset]
    epochs = int(os.environ.get("BENCH_EPOCHS", epochs))  # only for timing trials
    raw, missing = load()
    values = np.nan_to_num(raw.values(), nan=0.0)  # Uber 212 has one missing hour; 0 keeps every target a count
    series = raw.with_values(values).astype(np.float32)
    split = int(len(series) * 0.8)
    train = series[:split]
    # Every validation target lies after the split. TiDE and TFT take one input window from before it;
    # RNNModel scores whole shifted sequences, so its validation series starts one step before the split.
    val = series[split - 1 :] if model == "LSTM" else series[split - icl :]
    v = series.values()
    rec = Recorder()
    result = dict(dataset=dataset, model=model, seed=seed, lr=lr, epochs=epochs, icl=icl, ocl=ocl,
                  n_train=len(train), n_val_targets=len(series) - split, missing_set_to_zero=missing,
                  data_min=float(v.min()), data_max=float(v.max()), data_zero_fraction=float((v == 0).mean()),
                  **environment())
    t0 = time.time()
    with tempfile.TemporaryDirectory() as work_dir:
        m = build(model, icl, ocl, epochs, seed, lr, work_dir, rec)
        try:
            m.fit(train, val_series=val)
            result.update(status="finished")
        except Exception as e:  # a crash is a result here, recorded with where training was
            rec.raw.append(dict(STATS, partial_epoch=True))
            result.update(status="crashed", phase="fit", crash_epoch=rec.epoch, crash_batch=rec.batch,
                          error=f"{type(e).__name__}: {str(e).splitlines()[0][:300]}", traceback=traceback.format_exc())
        if result["status"] == "finished":
            try:
                MODE["name"] = "predict"
                _reset()
                pred = m.predict(n=ocl, series=train, num_samples=200).all_values()  # (time, component, sample)
                actual = series[split : split + ocl].values()
                result.update(forecast_mean=float(pred.mean()), forecast_zero_fraction=float((pred == 0).mean()),
                              forecast_mean_by_step=pred.mean(axis=(1, 2)).tolist(), actual_mean=float(actual.mean()),
                              predict_raw=dict(STATS))
            except Exception as e:
                result.update(status="crashed", phase="predict",
                              error=f"{type(e).__name__}: {str(e).splitlines()[0][:300]}", traceback=traceback.format_exc())
    result.update(seconds=round(time.time() - t0, 1), train_loss=rec.train, val_loss=rec.val,
                  variant=VARIANT or None, floor_x=FLOOR_X, raw_by_epoch=rec.raw)
    with open(out, "w") as f:
        json.dump(result, f)
    print(dataset, model, seed, lr, result["status"], len(rec.train), "epochs", result["seconds"], "s")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], int(sys.argv[3]), float(sys.argv[4]), sys.argv[5])
