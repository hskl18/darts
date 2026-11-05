# NegativeBinomialLikelihood benchmark for unit8co/darts#3322

This folder compares `master` at c828130 with the PR at d46a8b6.
Both trees train the same models on the same data, and each run records its train and val loss per epoch.

## Setup

- Data: three count series from `darts.datasets`, unscaled because the likelihood needs counts.
  The first 80% is the training series, and every validation target lies in the last 20%.
  - AirPassengers: monthly, 104 to 622, input 12, output 6, 200 epochs.
  - TaxiNewYork: every 30 minutes, 8 to about 39,200, input 96, output 48, 30 epochs.
  - UberTLC location 212: hourly, 0 to 7, about half zeros, input 48, output 24, 30 epochs.
    Its one missing hour is set to 0.
- Models: `TiDEModel`, `TFTModel` (`add_relative_index=True`) and `RNNModel(model="LSTM", training_length=input + output)`, batch size 32, otherwise default.
- Validation: TiDE and TFT get one input window from before the split, so they score blocks of `output` steps after it.
  `RNNModel` scores whole sequences shifted by one step, so its validation series starts one step before the split.
- Learning rates 1e-3 (the default), 1e-2 and 1e-1, seeds 0, 1 and 2, float32.
- Machine: Apple M4 Mac mini on CPU, one torch thread per run.
  Each JSON file records the Python, torch, Lightning, NumPy and pandas versions, the CPU and the darts commit it imported.

## What is measured

- Train loss: the mean over each epoch's batches, weighted by batch size.
  darts itself logs only each step's value, so `trainer.callback_metrics["train_loss"]` would be the last batch.
- Val loss: `val_loss` as darts logs it, the mean over the validation set.
- A run that stops with an error in training keeps the epochs it finished, the training epoch and batch it stopped in, and the full traceback.
  An error in `predict` would be recorded with its traceback only; none happened.
- Forecast: 200 samples for the `output` steps after the split, their mean divided by the actual mean of those steps, and the share of samples that are 0.

## Files

- `bench.py` trains one model and writes one JSON file.
- `run_all.sh` runs all 162 runs, 8 at a time, from its own folder.
- `plot.py` draws `plots/*.png` and prints `summary.md`.
  It checks that every result was produced by the darts tree and commit it is filed under.
- `results/existing` holds the `master` runs and `results/new` the PR runs.

## Rerunning

From a folder holding a darts clone that has the PR branch fetched, with these files next to it:

```sh
for v in existing:c8281305f788a0563112109d5f79cf2d4218d9e6 new:d46a8b6445310a6da14d4895b91697aadd5c5c4a; do
  git -C darts archive --prefix=${v%%:*}/ ${v#*:} darts pyproject.toml README.md LICENSE | tar x
  echo ${v#*:} > ${v%%:*}/COMMIT
done
uv venv -p 3.12 .venv
uv pip install -p .venv/bin/python "./new[torch]" "torch==2.14.1" "pytorch-lightning==2.6.6" "numpy==2.5.4" "pandas==3.1.1"
uv pip uninstall -p .venv/bin/python darts
zsh run_all.sh
.venv/bin/python plot.py results plots > summary.md
```

Each run imports darts from `existing/` or `new/` through `PYTHONPATH`.
