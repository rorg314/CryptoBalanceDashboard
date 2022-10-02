import datetime
import pandas as pd
import requests
import json
import time
from config import *

def CheckLastFetch(symbol):
    try:
        with open (PRICES_FOLDER +symbol+ r"_lastfetch.txt", 'r') as f:
            lastFetchLines = f.readlines()
            if(lastFetchLines):
                lastFetch = float(lastFetchLines[-1])
            now = time.time()
            if(now > lastFetch +1000):
                return True
            else: 
                return False
    except FileNotFoundError:
        with open (PRICES_FOLDER +symbol+ r"_lastfetch.txt", 'w+') as f:
            f.write('0')
            return True


def FetchDailyData(symbol):

    # TODO: Replace properly with better api implementation - for now just bypass the fetch and use the cached data only
    return

    # pair_split = symbol.split('/')  # symbol must be in format XXX/XXX ie. BTC/EUR
    # symbol = pair_split[0] + '-' + pair_split[1]
    # url = f'https://api.pro.coinbase.com/products/{symbol}/candles?granularity=86400'
    # response = requests.get(url)
    # if response.status_code == 200:  # check to make sure the response from server is good
    #     data = pd.DataFrame(json.loads(response.text), columns=['unix', 'low', 'high', 'open', 'close', 'volume'])
    #     # Reverse the dataframe so it goes from last -> today date 
    #     data = data.iloc[::-1]
    #     data['date'] = pd.to_datetime(data['unix'], unit='s')  # convert to a readable date
    #     data['vol_fiat'] = data['volume'] * data['close']      # multiply the BTC volume by closing price to approximate fiat volume

    #     # if we failed to get any data, print an error...otherwise write the file
    #     if data is None:
    #         print("Did not return any data from Coinbase for this symbol")
    #     else:
    #         data.to_csv(ROOTPATH + f'/CoinbaseProcessing/Prices/Coinbase_{pair_split[0] + pair_split[1]}_dailydata.csv', index=False)
    #         with open (PRICES_FOLDER +symbol+ r"_lastfetch.txt", 'w+') as f:
    #             lastFetch = f.write(str(time.time()))
    # else:
    #     print("Did not receieve OK response from Coinbase API")

def JSONPriceData(symbol):
    pair_split = symbol.split('/')  # symbol must be in format XXX/XXX ie. BTC/EUR
    symbol = pair_split[0] + '-' + pair_split[1]
    dataPath = ROOTPATH + r"/CoinbaseProcessing/Prices/Coinbase_" + pair_split[0] + pair_split[1] + r"_dailydata.csv"
    priceData = pd.read_csv(dataPath)
    dateHighLowDict = {date:(high,low) for date, (high, low) in zip(priceData['date'].to_list(), [highLow for highLow in zip(priceData['high'].to_list(), priceData['low'].to_list())])}
    outPath = PRICES_FOLDER + symbol + r"_DailyPrices_YTD.JSON"
    JSON = json.dumps(dateHighLowDict)
    with open(outPath, 'w+') as f:
        f.write(JSON)
    

def FetchCachedPriceData(pairs):

    for pair in pairs:
        pair_split = pair.split('/')  # symbol must be in format XXX/XXX ie. BTC/EUR
        symbol = pair_split[0] + '-' + pair_split[1]
        if(CheckLastFetch(symbol)):
            FetchDailyData(symbol=pair)
        JSONPriceData(symbol=pair)

              