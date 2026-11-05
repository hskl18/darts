#!/bin/zsh
# Runs the whole matrix from this script's folder, 8 runs at a time:
# results/<variant>/<dataset>_<model>_lr<lr>_s<seed>.json, where existing/ and new/ hold the two darts trees.
set -eu
cd "${0:A:h}"
mkdir -p results/existing results/new logs
for v in existing new; do for d in taxi_new_york uber_tlc_212 air_passengers; do for m in TFT LSTM TiDE; do
  for lr in 0.001 0.01 0.1; do for s in 0 1 2; do
    echo "$v $d $m $s $lr"
  done; done
done; done; done > jobs.txt
wc -l < jobs.txt
# a training crash is recorded in the JSON; only a failure of bench.py itself fails the run
if xargs -P 8 -L 1 zsh -c 'PYTHONPATH=$0 .venv/bin/python bench.py $1 $2 $3 $4 results/$0/$1_$2_lr$4_s$3.json > logs/$0_$1_$2_lr$4_s$3.log 2>&1' < jobs.txt; then
  echo ALL_DONE
else
  echo FAILED
  exit 1
fi
