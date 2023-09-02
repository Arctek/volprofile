#py download-aggTrade.py -s BTCUSDT  -t spot -skip-daily 1 -y 2023 -m 7

import pandas as pd
import numpy as np 
from zipfile import ZipFile
import math
import json

def create_point_of_control_from_dataframe(data):
    # Calculate the price range for binning
    min_price = data['price'].min()
    max_price = data['price'].max()
    price_range = max_price - min_price

    bin_size = 2*round(math.log(price_range),0)
    num_bins = int(price_range/bin_size)

    # Create the bins
    bins = [min_price + i * bin_size for i in range(num_bins + 1)]

    # Bin the data and calculate total volume for each bin
    volume_profile = []
    for i in range(num_bins):
        bin_data = data[(data['price'] >= bins[i]) & (data['price'] < bins[i+1])]
        total_volume = bin_data['quantity'].sum()      
        volume_profile.append(total_volume)

    poc_index = np.argmax(volume_profile)
    point_of_control = bins[poc_index]
    
    return point_of_control

if __name__=="__main__":
    df = pd.read_csv(ZipFile("../data/spot/monthly/aggTrades/BTCUSDT/BTCUSDT-aggTrades-2023-07.zip").open("BTCUSDT-aggTrades-2023-07.csv"), names=["aggregated_id","price","quantity","first_trade_id","last_trade_id","last_timestamp","is_buyer_maker","is_best_match"])
    #convert to datetime object from int
    df["datetime_object"] = pd.to_datetime(df['last_timestamp'], unit='ms')
    #convert to date object
    df["date"] = df["datetime_object"].dt.date
    #take the unique dates
    dates = df["date"].unique()
    #create a list of dictionaries with date and poc
    poc_list = []
    for date in dates:
        poc_list.append({'date':date.strftime("%Y-%m-%dT%H:%M:%S.%fZ"),'npoc':create_point_of_control_from_dataframe(df[df["date"] == date])})
    #save the list of dictionaries to a json file    
    with open('poclist.json', 'w') as f:
        json.dump(poc_list, f)