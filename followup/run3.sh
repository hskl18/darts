#!/bin/zsh
# UberTLC reruns with the float64 val loss: label:tree:variant dataset model seed lr -> results3/<label>/...
set -eu
cd "${0:A:h}"
mkdir -p results3/existing results3/new results3/logmu logs3
: > jobs3.txt
for s in 0 1 2; do for lr in 0.001 0.01 0.1; do for m in TiDE LSTM; do
  for v in existing:existing: new:new: logmu:new:logmu; do echo "${v} uber_tlc_212 $m $s $lr" >> jobs3.txt; done
done; done; done
wc -l < jobs3.txt
if xargs -P 8 -L 1 zsh -c 'IFS=: read l t v <<< "$0"; BENCH_VARIANT=$v PYTHONPATH=$t .venv/bin/python bench3.py $1 $2 $3 $4 results3/$l/$1_$2_lr$4_s$3.json > logs3/$l_$1_$2_lr$4_s$3.log 2>&1' < jobs3.txt; then
  echo ALL_DONE
else
  echo FAILED
  exit 1
fi
