# Follow-up checks

These runs answer three questions about the first benchmark.
They use the setup of the top-level README: run the scripts from a folder holding `existing/`, `new/` and `.venv`.

- `bench2.py` is `bench.py` plus per-epoch counts of raw mean and dispersion outputs below the PR's floor (about -15.94, where softplus gives float32 eps).
  With `BENCH_VARIANT=logmu` it also swaps in a variant that keeps the mean in log space with no floor and floors only `alpha`.
  `run2.sh` runs UberTLC with TiDE and LSTM, and AirPassengers and TaxiNewYork with TiDE, for `master`, the PR and the variant.
  `analysis2.md` is the output of `analyze2.py`.
- `bench3.py` is `bench2.py` plus the val loss recomputed in float64 at the same float32 parameters.
  `run3.sh` reruns the UberTLC part, and `analysis3.md` is the output of `analyze3.py`.

The reruns of `master` and the PR reproduce the losses in `results/` exactly; both analysis scripts check that.
