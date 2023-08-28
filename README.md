# Custom Volume Profile Indicator

This is a simple script that generates an accurate volume profile based on Binance API

## Extracting Custom Data

Before starting to use the indicator, download your desired amount of data. The command below obtains the aggregate trades for July 2023

```python
python download-aggTrade.py -s BTCUSDT -startDate 2023-07-01 -endDate 2023-07-31  -t spot -skip-monthly 1
```

## Getting Started

1. Go to /vol-profile/volprofilenotebook.ipynb
2. Replace the values from where the dataframe is created with your own

```python
df = pd.read_csv(ZipFile("PATH_TO_YOUR_DATA").open("BTCUSDT-aggTrades-YYYY-MM-DD.csv"), names=["aggregated_id","price","quantity","first_trade_id","last_trade_id","last_timestamp","is_buyer_maker","is_best_match"])
```

3. Run will provide a volume profile for the day selected in step 2
