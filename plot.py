"""Plot train/val loss per epoch from results/<variant>/*.json and print a summary table.

usage: python plot.py <results dir> <out dir>
"""

import glob
import json
import math
import os
import sys
from collections import defaultdict

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.lines import Line2D  # noqa: E402

RESULTS, OUT = sys.argv[1], sys.argv[2]
os.makedirs(OUT, exist_ok=True)
VARIANTS = {"existing": ("master c828130", "tab:orange", 3.0, 0.45), "new": ("PR d46a8b6", "tab:blue", 1.2, 1.0)}
COMMITS = {"existing": "c8281305f788a0563112109d5f79cf2d4218d9e6", "new": "d46a8b6445310a6da14d4895b91697aadd5c5c4a"}
MODELS = ["TiDE", "TFT", "LSTM"]
LRS = [0.001, 0.01, 0.1]
TITLES = {
    "air_passengers": "AirPassengers (monthly, 104 to 622)",
    "taxi_new_york": "TaxiNewYork (30 min, 8 to about 39,200)",
    "uber_tlc_212": "UberTLC location 212 (hourly, 0 to 7, half zeros)",
}

runs = defaultdict(list)  # (dataset, model, lr, variant) -> results
for path in glob.glob(os.path.join(RESULTS, "*", "*.json")):
    r = json.load(open(path))
    variant = os.path.basename(os.path.dirname(path))
    # the run imported darts from the tree it is filed under, and that tree is the named commit
    assert f"/{variant}/darts/" in r["darts_file"] and r["darts_commit"] == COMMITS[variant], (path, r["darts_commit"])
    runs[(r["dataset"], r["model"], r["lr"], variant)].append(r)


def finite(xs):
    return [x if x is not None and math.isfinite(x) else math.nan for x in xs]


rows = []
for dataset, title in TITLES.items():
    fig, axes = plt.subplots(len(MODELS), len(LRS), figsize=(15, 11), squeeze=False)
    for i, model in enumerate(MODELS):
        for j, lr in enumerate(LRS):
            ax = axes[i][j]
            crashes = {}
            for variant, (label, color, lw, alpha) in VARIANTS.items():
                rs = sorted(runs[(dataset, model, lr, variant)], key=lambda r: r["seed"])
                crashes[variant] = sum(r["status"] == "crashed" for r in rs), len(rs)
                for r in rs:
                    tr, va = finite(r["train_loss"]), finite(r["val_loss"])
                    ax.plot(range(1, len(tr) + 1), tr, color=color, lw=lw, alpha=alpha)
                    ax.plot(range(1, len(va) + 1), va, color=color, lw=lw, alpha=alpha, ls="--")
                    if r["status"] == "crashed":
                        assert r["phase"] == "fit", r  # every recorded crash so far is in training; a predict crash needs its own marker
                        # at the epoch it stopped in, near the bottom of the panel, so a loss-free crash keeps the y range
                        tf = ax.get_xaxis_transform()
                        ax.plot(r["crash_epoch"], 0.06, "X", color=color, ms=11, mec="black", transform=tf)
                        ax.text(r["crash_epoch"], 0.13 + 0.07 * r["seed"], f"seed {r['seed']}", fontsize=7, transform=tf)
                    rows.append((dataset, model, lr, variant, r))
            ax.set_yscale("log")
            ax.set_title(f"{model}, lr={lr:g}: crashed {crashes['existing'][0]}/{crashes['existing'][1]} on master, "
                         f"{crashes['new'][0]}/{crashes['new'][1]} with the PR", fontsize=9)
            if i == len(MODELS) - 1:
                ax.set_xlabel("epoch")
            if j == 0:
                ax.set_ylabel("NB negative log-likelihood")
    handles = [Line2D([], [], color=c, lw=lw, alpha=a, label=l) for l, c, lw, a in VARIANTS.values()]
    handles += [Line2D([], [], color="gray", label="train loss"), Line2D([], [], color="gray", ls="--", label="val loss"),
                Line2D([], [], marker="X", color="gray", mec="black", ls="", ms=10, label="ValueError, training stopped in this epoch")]
    fig.legend(handles=handles, loc="lower center", ncol=5, frameon=False)
    fig.suptitle(f"{title}: NegativeBinomialLikelihood, float32, CPU, seeds 0 to 2\n"
                 "train loss: mean over each epoch's batches; val loss: mean over the validation targets after the split", fontsize=11)
    fig.tight_layout(rect=(0, 0.04, 1, 0.97))
    fig.savefig(os.path.join(OUT, f"{dataset}.png"), dpi=110)
    plt.close(fig)

# summary: one line per dataset/model/lr/variant, final losses as min..max over seeds
print("| dataset | model | lr | code | crashed (epoch) | final train loss | final val loss | forecast mean / actual mean | zero samples in forecast |")
print("|---|---|---|---|---|---|---|---|---|")
groups = defaultdict(list)
for dataset, model, lr, variant, r in rows:
    groups[(dataset, model, lr, variant)].append(r)


def span(xs):
    xs = [x for x in xs if x is not None and math.isfinite(x)]
    return "-" if not xs else f"{min(xs):.4g}" if min(xs) == max(xs) else f"{min(xs):.4g} to {max(xs):.4g}"


for dataset in TITLES:
    for model in MODELS:
        for lr in LRS:
            for variant in VARIANTS:
                rs = groups[(dataset, model, lr, variant)]
                done = [r for r in rs if r["status"] == "finished"]
                crashed = [r for r in rs if r["status"] == "crashed"]
                epochs = ",".join(str(r["crash_epoch"]) for r in crashed)
                ratio = span([r["forecast_mean"] / r["actual_mean"] for r in done])
                zeros = span([r["forecast_zero_fraction"] for r in done])
                print(f"| {dataset} | {model} | {lr:g} | {VARIANTS[variant][0]} | {len(crashed)}/{len(rs)}"
                      f"{' (epoch ' + epochs + ')' if crashed else ''} | {span([r['train_loss'][-1] for r in done])}"
                      f" | {span([r['val_loss'][-1] for r in done if r['val_loss']])} | {ratio} | {zeros} |")
errors = sorted({f"{r['phase']}: {r['error']}" for *_, r in rows if r["status"] == "crashed"})
print("\nerrors:", *errors, sep="\n- ")
print("seconds:", round(sum(r["seconds"] for *_, r in rows)), "runs:", len(rows))
