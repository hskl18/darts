reruns: 72 mismatch with published: none

pairs where both finished: first differing epoch vs first epoch with a raw output below the floor (PR run)
  uber_tlc_212_LSTM_lr0.01_s0: split at 7, floor first acts at 7 (alpha)
  uber_tlc_212_LSTM_lr0.01_s1: split at 7, floor first acts at 7 (alpha)
  uber_tlc_212_LSTM_lr0.01_s2: split at 6, floor first acts at 6 (alpha)
  uber_tlc_212_LSTM_lr0.1_s0: split at 18, floor first acts at 18 (alpha)
  uber_tlc_212_LSTM_lr0.1_s1: split at 7, floor first acts at 7 (alpha)
  uber_tlc_212_TiDE_lr0.001_s0: split at 8, floor first acts at 8 (alpha)
  uber_tlc_212_TiDE_lr0.001_s1: split at 8, floor first acts at 8 (alpha)
  uber_tlc_212_TiDE_lr0.001_s2: split at 9, floor first acts at 9 (alpha)
  uber_tlc_212_TiDE_lr0.01_s0: split at 15, floor first acts at 15 (alpha)
  uber_tlc_212_TiDE_lr0.01_s2: split at 11, floor first acts at 11 (alpha)
  14 of 14 pairs agree (identical pairs have no floor activity)

| config | master | PR | logmu | PR zero samples | logmu zero samples | PR fc/actual | logmu fc/actual | PR final val | logmu final val | master final val |
|---|---|---|---|---|---|---|---|---|---|---|
| air_passengers_TiDE_lr0.001_s0 | crash e1 | ok | ok | 0.664 | 0.494 | 0.401 | 0.684 | 12.32 | 10.61 | - |
| air_passengers_TiDE_lr0.001_s1 | crash e1 | ok | ok | 0.158 | 0.166 | 1.42 | 1.01 | 8.65 | 8.972 | - |
| air_passengers_TiDE_lr0.001_s2 | crash e1 | ok | ok | 0.661 | 0.313 | 8.68 | 1.53 | 12.14 | 9.093 | - |
| air_passengers_TiDE_lr0.01_s0 | crash e1 | ok | ok | 1.000 | 1.000 | 0 | 0 | 159.7 | 20.23 | - |
| air_passengers_TiDE_lr0.01_s1 | crash e1 | ok | ok | 1.000 | 1.000 | 0 | 0 | 24.36 | 19.35 | - |
| air_passengers_TiDE_lr0.01_s2 | crash e1 | ok | ok | 1.000 | 0.999 | 0 | 0.247 | 29.87 | 17.84 | - |
| air_passengers_TiDE_lr0.1_s0 | crash e1 | ok | ok | 1.000 | 0.000 | 0 | 2.95e+07 | 29.11 | 5.913e+07 | - |
| air_passengers_TiDE_lr0.1_s1 | crash e1 | ok | ok | 1.000 | 0.667 | 0 | 6.32e+05 | 29.12 | 1.268e+07 | - |
| air_passengers_TiDE_lr0.1_s2 | crash e1 | ok | ok | 1.000 | 0.167 | 0 | 1.41e+08 | 29.14 | 6.034e+07 | - |
| taxi_new_york_TiDE_lr0.001_s0 | crash e1 | ok | ok | 0.917 | 0.896 | 0.0826 | 0.0943 | 1248 | 403.1 | - |
| taxi_new_york_TiDE_lr0.001_s1 | crash e1 | ok | ok | 0.875 | 0.792 | 0.111 | 0.222 | 2156 | 1531 | - |
| taxi_new_york_TiDE_lr0.001_s2 | crash e1 | ok | ok | 0.625 | 0.729 | 0.405 | 9.74 | 804.7 | 3591 | - |
| taxi_new_york_TiDE_lr0.01_s0 | crash e1 | ok | ok | 1.000 | 0.250 | 0 | 1.17e+05 | 35.83 | 3.491e+07 | - |
| taxi_new_york_TiDE_lr0.01_s1 | crash e1 | ok | ok | 1.000 | 0.000 | 0 | 5.78e+05 | 35.8 | 5.725e+07 | - |
| taxi_new_york_TiDE_lr0.01_s2 | crash e1 | ok | ok | 1.000 | 0.771 | 0 | 1.48e+04 | 35.81 | 8.81e+06 | - |
| taxi_new_york_TiDE_lr0.1_s0 | crash e1 | ok | ok | 1.000 | 0.000 | 0 | 2.06e+10 | 35.79 | 1.446e+08 | - |
| taxi_new_york_TiDE_lr0.1_s1 | crash e1 | ok | ok | 1.000 | 0.000 | 0 | 5.99e+10 | 35.83 | 1.539e+08 | - |
| taxi_new_york_TiDE_lr0.1_s2 | crash e1 | ok | ok | 1.000 | 0.000 | 0 | 1.96e+11 | 35.79 | 1.645e+08 | - |
| uber_tlc_212_LSTM_lr0.001_s0 | ok | ok | ok | 0.521 | 0.502 | 0.612 | 0.642 | 1.337 | 1.333 | 1.337 |
| uber_tlc_212_LSTM_lr0.001_s1 | ok | ok | ok | 0.540 | 0.547 | 0.577 | 0.575 | 1.34 | 1.34 | 1.34 |
| uber_tlc_212_LSTM_lr0.001_s2 | ok | ok | ok | 0.466 | 0.483 | 0.741 | 0.705 | 1.416 | 1.416 | 1.416 |
| uber_tlc_212_LSTM_lr0.01_s0 | ok | ok | ok | 0.579 | 0.439 | 0.63 | 1.24 | 1.693 | 1.722 | 1.863 |
| uber_tlc_212_LSTM_lr0.01_s1 | ok | ok | ok | 0.351 | 0.555 | 1.97 | 0.677 | 1.57 | 1.599 | 1.805 |
| uber_tlc_212_LSTM_lr0.01_s2 | ok | ok | ok | 0.575 | 0.573 | 0.621 | 0.693 | 1.58 | 1.715 | 1.858 |
| uber_tlc_212_LSTM_lr0.1_s0 | ok | ok | ok | 0.398 | 0.441 | 0.779 | 0.699 | 0.9922 | 0.9913 | 1.111 |
| uber_tlc_212_LSTM_lr0.1_s1 | ok | ok | ok | 0.415 | 0.493 | 0.837 | 0.598 | 1.337 | 1.009 | 1.333 |
| uber_tlc_212_LSTM_lr0.1_s2 | ok | ok | ok | 0.532 | 0.500 | 0.587 | 0.594 | 1.339 | 1.019 | 1.339 |
| uber_tlc_212_TiDE_lr0.001_s0 | ok | ok | ok | 0.674 | 0.620 | 0.381 | 0.455 | 1.271 | 1.268 | 1.827 |
| uber_tlc_212_TiDE_lr0.001_s1 | ok | ok | ok | 0.645 | 0.610 | 0.436 | 0.509 | 1.264 | 1.265 | 1.863 |
| uber_tlc_212_TiDE_lr0.001_s2 | ok | ok | ok | 0.670 | 0.631 | 0.383 | 0.459 | 1.246 | 1.241 | 1.834 |
| uber_tlc_212_TiDE_lr0.01_s0 | ok | ok | ok | 0.375 | 0.403 | 0.847 | 0.806 | 1.024 | 1.04 | 1.367 |
| uber_tlc_212_TiDE_lr0.01_s1 | crash e15 | ok | ok | 0.442 | 0.412 | 0.69 | 0.771 | 1.023 | 1.012 | - |
| uber_tlc_212_TiDE_lr0.01_s2 | ok | ok | ok | 0.454 | 0.492 | 0.712 | 0.614 | 1.022 | 1.035 | 1.373 |
| uber_tlc_212_TiDE_lr0.1_s0 | crash e1 | ok | ok | 1.000 | 1.000 | 0 | 0.0019 | 10.21 | 9.019 | - |
| uber_tlc_212_TiDE_lr0.1_s1 | crash e1 | ok | ok | 1.000 | 1.000 | 0 | 0 | 10.2 | 8.426 | - |
| uber_tlc_212_TiDE_lr0.1_s2 | crash e1 | ok | ok | 1.000 | 1.000 | 0 | 0 | 10.28 | 7.8 | - |

logmu vs master where master finished:
  uber_tlc_212_LSTM_lr0.001_s0: differs from epoch 1, final val master 1.337 logmu 1.333
  uber_tlc_212_LSTM_lr0.001_s1: differs from epoch 1, final val master 1.34 logmu 1.34
  uber_tlc_212_LSTM_lr0.001_s2: differs from epoch 1, final val master 1.416 logmu 1.416
  uber_tlc_212_LSTM_lr0.01_s0: differs from epoch 1, final val master 1.863 logmu 1.722
  uber_tlc_212_LSTM_lr0.01_s1: differs from epoch 1, final val master 1.805 logmu 1.599
  uber_tlc_212_LSTM_lr0.01_s2: differs from epoch 2, final val master 1.858 logmu 1.715
  uber_tlc_212_LSTM_lr0.1_s0: differs from epoch 1, final val master 1.111 logmu 0.9913
  uber_tlc_212_LSTM_lr0.1_s1: differs from epoch 1, final val master 1.333 logmu 1.009
  uber_tlc_212_LSTM_lr0.1_s2: differs from epoch 1, final val master 1.339 logmu 1.019
  uber_tlc_212_TiDE_lr0.001_s0: differs from epoch 1, final val master 1.827 logmu 1.268
  uber_tlc_212_TiDE_lr0.001_s1: differs from epoch 1, final val master 1.863 logmu 1.265
  uber_tlc_212_TiDE_lr0.001_s2: differs from epoch 1, final val master 1.834 logmu 1.241
  uber_tlc_212_TiDE_lr0.01_s0: differs from epoch 1, final val master 1.367 logmu 1.04
  uber_tlc_212_TiDE_lr0.01_s2: differs from epoch 1, final val master 1.373 logmu 1.035
existing: 36 runs, 22 crashed, 0 with every forecast sample 0
new: 36 runs, 0 crashed, 15 with every forecast sample 0
logmu: 36 runs, 0 crashed, 4 with every forecast sample 0
seconds: 1436
