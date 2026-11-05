reruns match published; max relative gap between recomputed and logged float32 val loss: 2.49e-07

| run | master val f32 | master val f64 | PR val f32 | PR val f64 | logmu val f32 | logmu val f64 |
|---|---|---|---|---|---|---|
| uber_tlc_212_LSTM_lr0.001_s0 | 1.3372 | 1.3372 | 1.3372 | 1.3372 | 1.3332 | 1.3332 |
| uber_tlc_212_LSTM_lr0.001_s1 | 1.3404 | 1.3404 | 1.3404 | 1.3404 | 1.3401 | 1.3401 |
| uber_tlc_212_LSTM_lr0.001_s2 | 1.4156 | 1.4156 | 1.4156 | 1.4156 | 1.4157 | 1.4157 |
| uber_tlc_212_LSTM_lr0.01_s0 | 1.8625 | 1.9162 | 1.6927 | 1.9337 | 1.7221 | 1.9379 |
| uber_tlc_212_LSTM_lr0.01_s1 | 1.8055 | 1.8209 | 1.5697 | 1.8056 | 1.5993 | 1.8085 |
| uber_tlc_212_LSTM_lr0.01_s2 | 1.8584 | 1.8583 | 1.5802 | 1.8298 | 1.7153 | 1.9509 |
| uber_tlc_212_LSTM_lr0.1_s0 | 1.1112 | 1.3560 | 0.9922 | 1.3445 | 0.9913 | 1.3431 |
| uber_tlc_212_LSTM_lr0.1_s1 | 1.3325 | 1.3325 | 1.3370 | 1.3370 | 1.0095 | 1.3617 |
| uber_tlc_212_LSTM_lr0.1_s2 | 1.3389 | 1.3389 | 1.3389 | 1.3389 | 1.0188 | 1.3711 |
| uber_tlc_212_TiDE_lr0.001_s0 | 1.8273 | 1.8273 | 1.2709 | 1.6197 | 1.2675 | 1.6093 |
| uber_tlc_212_TiDE_lr0.001_s1 | 1.8630 | 1.8631 | 1.2639 | 1.6087 | 1.2653 | 1.6116 |
| uber_tlc_212_TiDE_lr0.001_s2 | 1.8342 | 1.8344 | 1.2460 | 1.5933 | 1.2410 | 1.5882 |
| uber_tlc_212_TiDE_lr0.01_s0 | 1.3670 | 1.3670 | 1.0240 | 1.3754 | 1.0403 | 1.3885 |
| uber_tlc_212_TiDE_lr0.01_s1 | - | - | 1.0232 | 1.3745 | 1.0122 | 1.3635 |
| uber_tlc_212_TiDE_lr0.01_s2 | 1.3732 | 1.3732 | 1.0217 | 1.3727 | 1.0350 | 1.3853 |
| uber_tlc_212_TiDE_lr0.1_s0 | - | - | 10.2136 | 10.2136 | 9.0189 | 9.0189 |
| uber_tlc_212_TiDE_lr0.1_s1 | - | - | 10.2046 | 10.2046 | 8.4262 | 8.4262 |
| uber_tlc_212_TiDE_lr0.1_s2 | - | - | 10.2790 | 10.2790 | 7.7996 | 7.7996 |

differing pairs: 10; PR final val lower in float32: 9, in float64: 7
largest |float32 - float64| val loss over all epochs: {'existing': 0.2944, 'new': 0.3526, 'logmu': 0.3542}
