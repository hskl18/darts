"""Final val loss as darts logs it (float32) vs recomputed in float64, for the UberTLC runs in results3/.

usage: python analyze3.py <results3 dir> <published results dir>
"""

import json
import os
import sys

R3, PUB = sys.argv[1], sys.argv[2]
runs = {v: {f[:-5]: json.load(open(os.path.join(R3, v, f))) for f in os.listdir(os.path.join(R3, v)) if f.endswith(".json")}
        for v in ("existing", "new", "logmu")}

# reruns still match the published losses, and the recomputed float32 val loss matches the logged one
for v in ("existing", "new"):
    for k, r in runs[v].items():
        p = json.load(open(os.path.join(PUB, v, k + ".json")))
        assert (r["train_loss"], r["val_loss"]) == (p["train_loss"], p["val_loss"]), (v, k)
worst = max(abs(a - b) / abs(b) for v in runs for r in runs[v].values() for a, b in zip(r["val_loss32_recomputed"], r["val_loss"]))
print("reruns match published; max relative gap between recomputed and logged float32 val loss:", f"{worst:.2e}")

print("\n| run | master val f32 | master val f64 | PR val f32 | PR val f64 | logmu val f32 | logmu val f64 |")
print("|---|---|---|---|---|---|---|")
lower32 = lower64 = pairs = 0
worst_err = {v: 0.0 for v in runs}
for k in sorted(runs["new"]):
    e, n, l = runs["existing"][k], runs["new"][k], runs["logmu"][k]

    def f(r, key):
        return r[key][-1] if r["status"] == "finished" and r[key] else None

    for v, r in (("existing", e), ("new", n), ("logmu", l)):
        for a, b in zip(r["val_loss"], r["val_loss64"]):
            worst_err[v] = max(worst_err[v], abs(a - b))
    cells = [f(r, key) for r in (e, n, l) for key in ("val_loss", "val_loss64")]
    print(f"| {k} | " + " | ".join("-" if c is None else f"{c:.4f}" for c in cells) + " |")
    if e["status"] == n["status"] == "finished" and e["val_loss"] != n["val_loss"]:
        pairs += 1
        lower32 += n["val_loss"][-1] < e["val_loss"][-1]
        lower64 += n["val_loss64"][-1] < e["val_loss64"][-1]
print(f"\ndiffering pairs: {pairs}; PR final val lower in float32: {lower32}, in float64: {lower64}")
print("largest |float32 - float64| val loss over all epochs:", {v: round(x, 4) for v, x in worst_err.items()})
