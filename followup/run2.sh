#!/bin/zsh
# Follow-up runs: label tree variant dataset model seed lr -> results2/<label>/<dataset>_<model>_lr<lr>_s<seed>.json
set -eu
cd "${0:A:h}"
mkdir -p results2/existing results2/new results2/logmu logs2
: > jobs2.txt
for s in 0 1 2; do for lr in 0.001 0.01 0.1; do
  for m in TiDE LSTM; do
    for v in existing:existing: new:new: logmu:new:logmu; do echo "${v} uber_tlc_212 $m $s $lr" >> jobs2.txt; done
  done
  for d in air_passengers taxi_new_york; do
    for v in existing:existing: new:new: logmu:new:logmu; do echo "${v} $d TiDE $s $lr" >> jobs2.txt; done
  done
done; done
wc -l < jobs2.txt
# each line: label:tree:variant dataset model seed lr
if xargs -P 8 -L 1 zsh -c 'IFS=: read l t v <<< "$0"; BENCH_VARIANT=$v PYTHONPATH=$t .venv/bin/python bench2.py $1 $2 $3 $4 results2/$l/$1_$2_lr$4_s$3.json > logs2/$l_$1_$2_lr$4_s$3.log 2>&1' < jobs2.txt; then
  echo ALL_DONE
else
  echo FAILED
  exit 1
fi
