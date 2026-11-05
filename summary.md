| dataset | model | lr | code | crashed (epoch) | final train loss | final val loss | forecast mean / actual mean | zero samples in forecast |
|---|---|---|---|---|---|---|---|---|
| air_passengers | TiDE | 0.001 | master c828130 | 3/3 (epoch 1,1,1) | - | - | - | - |
| air_passengers | TiDE | 0.001 | PR d46a8b6 | 0/3 | 9.033 to 11.72 | 8.65 to 12.32 | 0.4008 to 8.677 | 0.1575 to 0.6642 |
| air_passengers | TiDE | 0.01 | master c828130 | 3/3 (epoch 1,1,1) | - | - | - | - |
| air_passengers | TiDE | 0.01 | PR d46a8b6 | 0/3 | 29.61 to 552.1 | 24.36 to 159.7 | 0 | 1 |
| air_passengers | TiDE | 0.1 | master c828130 | 3/3 (epoch 1,1,1) | - | - | - | - |
| air_passengers | TiDE | 0.1 | PR d46a8b6 | 0/3 | 27.97 to 28.29 | 29.11 to 29.14 | 0 | 1 |
| air_passengers | TFT | 0.001 | master c828130 | 0/3 | 10.94 to 11.94 | 14.12 to 15.98 | 0.01767 to 0.02428 | 0.5692 to 0.5892 |
| air_passengers | TFT | 0.001 | PR d46a8b6 | 0/3 | 10.94 to 11.94 | 14.12 to 15.98 | 0.01767 to 0.02428 | 0.5692 to 0.5892 |
| air_passengers | TFT | 0.01 | master c828130 | 0/3 | 7.671 to 8.516 | 9.451 to 9.784 | 0.08216 to 0.1659 | 0.07167 to 0.5142 |
| air_passengers | TFT | 0.01 | PR d46a8b6 | 0/3 | 7.671 to 8.516 | 9.451 to 9.784 | 0.08216 to 0.1659 | 0.07167 to 0.5142 |
| air_passengers | TFT | 0.1 | master c828130 | 0/3 | 5.826 to 7.33 | 7.143 to 8.475 | 0.5467 to 0.6854 | 0 to 0.004167 |
| air_passengers | TFT | 0.1 | PR d46a8b6 | 0/3 | 5.826 to 7.33 | 7.143 to 8.475 | 0.5467 to 0.6854 | 0 to 0.004167 |
| air_passengers | LSTM | 0.001 | master c828130 | 0/3 | 11.37 to 14.23 | 15.54 to 21.08 | 0.01225 to 0.01724 | 0.5417 to 0.5567 |
| air_passengers | LSTM | 0.001 | PR d46a8b6 | 0/3 | 11.37 to 14.23 | 15.54 to 21.08 | 0.01225 to 0.01724 | 0.5417 to 0.5567 |
| air_passengers | LSTM | 0.01 | master c828130 | 0/3 | 8.91 to 9.556 | 10.42 to 11.79 | 0.02297 to 0.0477 | 0.5842 to 0.6342 |
| air_passengers | LSTM | 0.01 | PR d46a8b6 | 0/3 | 8.91 to 9.556 | 10.42 to 11.79 | 0.02297 to 0.0477 | 0.5842 to 0.6342 |
| air_passengers | LSTM | 0.1 | master c828130 | 0/3 | 7.244 to 8.186 | 8.691 to 9.813 | 0.09927 to 0.2322 | 0.08417 to 0.3508 |
| air_passengers | LSTM | 0.1 | PR d46a8b6 | 0/3 | 7.244 to 8.186 | 8.691 to 9.813 | 0.09927 to 0.2322 | 0.08417 to 0.3508 |
| taxi_new_york | TiDE | 0.001 | master c828130 | 3/3 (epoch 1,1,1) | - | - | - | - |
| taxi_new_york | TiDE | 0.001 | PR d46a8b6 | 0/3 | 552.4 to 9921 | 804.7 to 2156 | 0.08259 to 0.4052 | 0.6249 to 0.9167 |
| taxi_new_york | TiDE | 0.01 | master c828130 | 3/3 (epoch 1,1,1) | - | - | - | - |
| taxi_new_york | TiDE | 0.01 | PR d46a8b6 | 0/3 | 36.09 to 36.4 | 35.8 to 35.83 | 0 | 1 |
| taxi_new_york | TiDE | 0.1 | master c828130 | 3/3 (epoch 1,1,1) | - | - | - | - |
| taxi_new_york | TiDE | 0.1 | PR d46a8b6 | 0/3 | 36.06 to 36.32 | 35.79 to 35.83 | 0 | 1 |
| taxi_new_york | TFT | 0.001 | master c828130 | 0/3 | 18.44 to 21.07 | 17.6 to 19.84 | 0.002727 to 0.003284 | 0.8365 to 0.867 |
| taxi_new_york | TFT | 0.001 | PR d46a8b6 | 0/3 | 18.44 to 21.07 | 17.6 to 19.84 | 0.002727 to 0.003284 | 0.8365 to 0.867 |
| taxi_new_york | TFT | 0.01 | master c828130 | 0/3 | 14.38 to 14.82 | 14.05 to 14.55 | 0.01222 to 0.01914 | 0.8168 to 0.9058 |
| taxi_new_york | TFT | 0.01 | PR d46a8b6 | 0/3 | 14.38 to 14.82 | 14.05 to 14.55 | 0.01222 to 0.01914 | 0.8168 to 0.9058 |
| taxi_new_york | TFT | 0.1 | master c828130 | 2/3 (epoch 18,30) | 13.96 | 13.39 | 0.04168 | 0.752 |
| taxi_new_york | TFT | 0.1 | PR d46a8b6 | 0/3 | 13.96 to 21.33 | 13.39 to 14.6 | 0.01688 to 0.04168 | 0.752 to 0.9253 |
| taxi_new_york | LSTM | 0.001 | master c828130 | 0/3 | 157.2 to 280.1 | 137.2 to 243.6 | 0.0001881 to 0.0002446 | 0.4956 to 0.4995 |
| taxi_new_york | LSTM | 0.001 | PR d46a8b6 | 0/3 | 157.2 to 280.1 | 137.2 to 243.6 | 0.0001881 to 0.0002446 | 0.4956 to 0.4995 |
| taxi_new_york | LSTM | 0.01 | master c828130 | 0/3 | 36.43 to 53.1 | 33.02 to 47.37 | 0.0005368 to 0.0006117 | 0.6078 to 0.6429 |
| taxi_new_york | LSTM | 0.01 | PR d46a8b6 | 0/3 | 36.43 to 53.1 | 33.02 to 47.37 | 0.0005368 to 0.0006117 | 0.6078 to 0.6429 |
| taxi_new_york | LSTM | 0.1 | master c828130 | 0/3 | 18.07 to 20.67 | 17.28 to 19.49 | 0.001026 to 0.001342 | 0.7179 to 0.7649 |
| taxi_new_york | LSTM | 0.1 | PR d46a8b6 | 0/3 | 18.07 to 20.67 | 17.28 to 19.49 | 0.001026 to 0.001342 | 0.7179 to 0.7649 |
| uber_tlc_212 | TiDE | 0.001 | master c828130 | 0/3 | 0.8051 to 0.8229 | 1.827 to 1.863 | 0.3014 to 0.3733 | 0.6767 to 0.7556 |
| uber_tlc_212 | TiDE | 0.001 | PR d46a8b6 | 0/3 | 0.6929 to 0.709 | 1.246 to 1.271 | 0.381 to 0.4355 | 0.6448 to 0.6735 |
| uber_tlc_212 | TiDE | 0.01 | master c828130 | 1/3 (epoch 15) | 1.145 to 1.149 | 1.367 to 1.373 | 0.6897 to 0.791 | 0.4417 to 0.4792 |
| uber_tlc_212 | TiDE | 0.01 | PR d46a8b6 | 0/3 | 0.9464 to 0.9495 | 1.022 to 1.024 | 0.6903 to 0.8472 | 0.3748 to 0.454 |
| uber_tlc_212 | TiDE | 0.1 | master c828130 | 3/3 (epoch 1,1,1) | - | - | - | - |
| uber_tlc_212 | TiDE | 0.1 | PR d46a8b6 | 0/3 | 8.148 to 8.371 | 10.2 to 10.28 | 0 | 1 |
| uber_tlc_212 | TFT | 0.001 | master c828130 | 0/3 | 1.103 to 1.112 | 1.375 to 1.382 | 0.4595 to 0.494 | 0.5923 to 0.6088 |
| uber_tlc_212 | TFT | 0.001 | PR d46a8b6 | 0/3 | 1.103 to 1.112 | 1.375 to 1.382 | 0.4595 to 0.494 | 0.5923 to 0.6088 |
| uber_tlc_212 | TFT | 0.01 | master c828130 | 0/3 | 1.11 to 1.127 | 1.367 to 1.399 | 0.3148 to 0.7576 | 0.4348 to 0.7006 |
| uber_tlc_212 | TFT | 0.01 | PR d46a8b6 | 0/3 | 1.11 to 1.127 | 1.367 to 1.399 | 0.3148 to 0.7576 | 0.4348 to 0.7006 |
| uber_tlc_212 | TFT | 0.1 | master c828130 | 0/3 | 1.171 to 1.172 | 1.353 to 1.372 | 0.5862 to 0.6667 | 0.5012 to 0.5444 |
| uber_tlc_212 | TFT | 0.1 | PR d46a8b6 | 0/3 | 1.171 to 1.172 | 1.353 to 1.372 | 0.5862 to 0.6667 | 0.5012 to 0.5444 |
| uber_tlc_212 | LSTM | 0.001 | master c828130 | 0/3 | 1.079 to 1.1 | 1.337 to 1.416 | 0.5769 to 0.7405 | 0.466 to 0.5402 |
| uber_tlc_212 | LSTM | 0.001 | PR d46a8b6 | 0/3 | 1.079 to 1.1 | 1.337 to 1.416 | 0.5769 to 0.7405 | 0.466 to 0.5402 |
| uber_tlc_212 | LSTM | 0.01 | master c828130 | 0/3 | 0.791 to 0.8098 | 1.805 to 1.863 | 0.5457 to 0.8538 | 0.5025 to 0.6273 |
| uber_tlc_212 | LSTM | 0.01 | PR d46a8b6 | 0/3 | 0.6619 to 0.6945 | 1.57 to 1.693 | 0.6212 to 1.97 | 0.3506 to 0.5792 |
| uber_tlc_212 | LSTM | 0.1 | master c828130 | 0/3 | 0.9719 to 1.146 | 1.111 to 1.339 | 0.5869 to 0.7552 | 0.4062 to 0.5319 |
| uber_tlc_212 | LSTM | 0.1 | PR d46a8b6 | 0/3 | 0.916 to 1.145 | 0.9922 to 1.339 | 0.5869 to 0.8367 | 0.3981 to 0.5319 |

errors:
- fit: ValueError: Expected parameter total_count (Tensor of shape (32, 24, 1)) of distribution NegativeBinomial(total_count: torch.Size([32, 24, 1]), logits: torch.Size([32, 24, 1])) to satisfy the constraint GreaterThanEq(lower_bound=0), but found invalid values:
- fit: ValueError: Expected parameter total_count (Tensor of shape (32, 48, 1)) of distribution NegativeBinomial(total_count: torch.Size([32, 48, 1]), logits: torch.Size([32, 48, 1])) to satisfy the constraint GreaterThanEq(lower_bound=0), but found invalid values:
- fit: ValueError: Expected parameter total_count (Tensor of shape (32, 6, 1)) of distribution NegativeBinomial(total_count: torch.Size([32, 6, 1]), logits: torch.Size([32, 6, 1])) to satisfy the constraint GreaterThanEq(lower_bound=0), but found invalid values:
seconds: 8505 runs: 162
