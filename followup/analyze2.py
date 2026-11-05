"""Compare the follow-up runs (results2/{existing,new,logmu}) with the published ones (published/{existing,new}).

usage: python analyze2.py <results2 dir> <published results dir>
"""

import json
import math
import os
import sys
from collections import defaultdict

R2, PUB = sys.argv[1], sys.argv[2]


def load(d):
    out = {}
    for f in sorted(os.listdir(d)):
        if f.endswith(".json"):
            out[f[:-5]] = json.load(open(os.path.join(d, f)))
    return out


runs = {v: load(os.path.join(R2, v)) for v in ("existing", "new", "logmu")}
pub = {v: load(os.path.join(PUB, v)) for v in ("existing", "new")}

# 1. the instrumented reruns reproduce the published losses exactly
mismatch = [(v, k) for v in pub for k, r in runs[v].items()
            if (r["train_loss"], r["val_loss"], r["status"]) != (pub[v][k]["train_loss"], pub[v][k]["val_loss"], pub[v][k]["status"])]
print("reruns:", sum(len(runs[v]) for v in pub), "mismatch with published:", mismatch or "none")


def first_diff(a, b):
    for i, (x, y) in enumerate(zip(a, b)):
        if x != y:
            return i + 1
    return None if len(a) == len(b) else min(len(a), len(b)) + 1


def first_floor(r):
    for i, e in enumerate(r["raw_by_epoch"]):
        if e["mu_below"] or e["alpha_below"]:
            return i + 1, "mu" if e["mu_below"] else "alpha"
    return None, None


# 2. where master and the PR both finish: the curves split exactly in the epoch the floor first acts
print("\npairs where both finished: first differing epoch vs first epoch with a raw output below the floor (PR run)")
agree, rows = 0, 0
for k, e in runs["existing"].items():
    n = runs["new"][k]
    if e["status"] != "finished" or n["status"] != "finished":
        continue
    rows += 1
    d = first_diff(e["train_loss"], n["train_loss"]) or first_diff(e["val_loss"], n["val_loss"])
    f, which = first_floor(n)
    agree += d == f
    if d or f:
        print(f"  {k}: split at {d}, floor first acts at {f} ({which})")
print(f"  {agree} of {rows} pairs agree (identical pairs have no floor activity)")


def ratio(r):
    return r["forecast_mean"] / r["actual_mean"] if r["status"] == "finished" else math.nan


# 3. per config: master / PR / logmu
print("\n| config | master | PR | logmu | PR zero samples | logmu zero samples | PR fc/actual | logmu fc/actual | PR final val | logmu final val | master final val |")
print("|---|---|---|---|---|---|---|---|---|---|---|")
groups = defaultdict(dict)
for v in runs:
    for k, r in runs[v].items():
        groups[k][v] = r


def st(r):
    return "ok" if r["status"] == "finished" else f"crash e{r.get('crash_epoch')}"


def fv(r):
    return f"{r['val_loss'][-1]:.4g}" if r["status"] == "finished" and r["val_loss"] else "-"


summary = defaultdict(lambda: defaultdict(list))
for k in sorted(groups):
    g = groups[k]
    e, n, l = g["existing"], g["new"], g["logmu"]
    cfg = k.rsplit("_s", 1)[0]
    for v, r in g.items():
        summary[cfg][v].append(r)
    print(f"| {k} | {st(e)} | {st(n)} | {st(l)} | {n.get('forecast_zero_fraction', math.nan):.3f} | {l.get('forecast_zero_fraction', math.nan):.3f} "
          f"| {ratio(n):.3g} | {ratio(l):.3g} | {fv(n)} | {fv(l)} | {fv(e)} |")

# 4. logmu vs master where master finished: identical, or how close
print("\nlogmu vs master where master finished:")
for k, e in runs["existing"].items():
    l = runs["logmu"][k]
    if e["status"] == "finished":
        d = first_diff(e["train_loss"], l["train_loss"]) or first_diff(e["val_loss"], l["val_loss"])
        print(f"  {k}: {'identical' if d is None else f'differs from epoch {d}'}, final val master {fv(e)} logmu {fv(l)}")

# 5. counts
for v in runs:
    rs = list(runs[v].values())
    crashed = sum(r["status"] == "crashed" for r in rs)
    allzero = sum(r["status"] == "finished" and r["forecast_zero_fraction"] == 1.0 for r in rs)
    print(f"{v}: {len(rs)} runs, {crashed} crashed, {allzero} with every forecast sample 0")
print("seconds:", round(sum(r["seconds"] for v in runs for r in runs[v].values())))
