# Custom Volume Profile Indicator

This is a simple script that generates an accurate volume profile based on Binance API

## Extracting Custom Data

Before starting to use the indicator, download your desired amount of data. The command below obtains the aggregate trades for July 2023

```python
python download-aggTrade.py -s BTCUSDT -startDate 2023-07-01 -endDate 2023-07-31  -t spot -skip-monthly 1
```
