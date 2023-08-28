# Custom Volume Profile Indicator

This is a simple script that generates an accurate volume profile based on Binance API

## Extracting Custom Data

Before starting to use the indicator, download your desired amount of data. The command below obtains the aggregate trades for July 2023

```python
python3 binanace-data/download-aggTrade.py -s BTCUSDT -startDate 2023-07-01 -endDate 2023-07-31  -t spot -skip-monthly 1
```

## Getting Started

1. Go to /vol-profile/volprofilenotebook.ipynb
2. Replace the values from where the dataframe is created with your own. By default the path will be:

```python
df = pd.read_csvZipFile("../data/spot/daily/aggTrades/BTCUSDT/BTCUSDT-aggTrades-YYYY-MM-DD.zip".open("BTCUSDT-aggTrades-YYYY-MM-DD.csv"), names=["aggregated_id","price","quantity","first_trade_id","last_trade_id","last_timestamp","is_buyer_maker","is_best_match"])
```

3. Run will provide a volume profile for the day selected in step 2

## How the volume profile is calculated

Data for every trade is pulled from the Binance API. After that, the high and the low of the range are obtained in order to divide it in a certain amount of bins (set to 50 by default).

Next, the bin with the most volume is obtained, also called Point of Control (PoC). Lastly, to calculate the Value Area (or 1 STD parting from the PoC), values for the bins above and below the PoC are considered until the total volume reaches 68%.
