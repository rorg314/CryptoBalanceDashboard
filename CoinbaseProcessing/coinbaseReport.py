from cryptocompare.cryptocompare import Timestamp
import pandas as pd
from matplotlib import pyplot as plt
import cryptocompare
from datetime import datetime as dt
import datetime
import json
from time import mktime




# Build the dataframe from the report csv
def ExtractBalanceDataframe(reportPath):
    
    reportDataframe = pd.read_csv(reportPath)

    for col in reportDataframe.columns:
        if(isinstance(reportDataframe[col][0], str)):
            reportDataframe[col].str.lower()

    return reportDataframe

# Processing timestamp strings (YYYY-MM-DD T HH:MM:SS Z) into datetimes 
def DatetimeTimestamps(dataframe):
    raw = dataframe['Timestamp'].to_list()
    dateTimes = list()
    for time in raw:
        time = time.split('T')[0].replace('-', ' ').strip()
        dateTimes.append(dt.strptime(time, '%Y %m %d'))
    
    dataframe.drop('Timestamp', axis=1, inplace=True)
    dataframe['Timestamp'] = dateTimes
    return dataframe

# Use to extract the buy/sell data for an individual currency
def ExtractCurrencyData(reportDf, currencyStr="BTC"):

    assetList = reportDf['Asset']

    #Slice the dataframe by the asset 
    currencyDf = reportDf.loc[(reportDf['Asset'] == currencyStr)]

    # Slice by buy
    buyDf = currencyDf.loc[(currencyDf['Transaction Type'] == 'Buy')]

    # Slice by converts
    convertDf = currencyDf.loc[(currencyDf['Transaction Type'] == 'Convert') &(currencyDf['Fees'] > 0)]

    return FilterCurrencyData(currencyDf, buyDf, convertDf)



# Filter the data to only include those columns 
def FilterCurrencyData(currencyDf, buyDf, convertDf):
    includeCols = ['Timestamp', 'Quantity Transacted', 'Spot Price at Transaction', 'Subtotal',	'Total (inclusive of fees)', 'Fees']
    return DatetimeTimestamps(currencyDf.loc[:, includeCols]), DatetimeTimestamps(buyDf.loc[:, includeCols]), DatetimeTimestamps(convertDf.loc[:, includeCols])


def FormatUSDPrice(rawPrice):
    return f"{rawPrice:2.2f}"

# Process the buys into a dict of timestamp -> buy amount (accounts for buys on the same day which it did not previously)
def GetTimestampBuys()


# ======================================================== #
# ======================== CLASSES ======================= #
# ======================================================== #


class Coin():
    def __init__(self, name:str):
        # Name of the coin
        self.name = name
        # Symbol /USD
        self.symbol = self.name+"-USD"
        # Previous prices
        with open(r"./CryptoDashboardApp/Public/Prices/" + self.symbol + r"_DailyPrices_YTD.JSON") as f:
            self.dateHighLow = json.loads(f.readline())
        self.datePriceHighs = {date:price for date, price in zip(list(self.dateHighLow.keys()), [price[0] for price in list(self.dateHighLow.values())])}
        self.datePriceLows = {date:price for date, price in zip(list(self.dateHighLow.keys()), [price[1] for price in list(self.dateHighLow.values())])}




class ReportData():
    def __init__(self, reportPath="./CoinbaseProcessing/Report.csv"):
        self.reportDf = ExtractBalanceDataframe(reportPath)
        self.currencies = ['BTC', 'ETH', 'DOGE']
        
        # Build individual currency data from report dataframe
        self.currencyData, self.buyData, self.convertData = dict(), dict(), dict()
        for currency in self.currencies:
            self.currencyData[currency], self.buyData[currency], self.convertData[currency] = ExtractCurrencyData(self.reportDf, currency)

             
        

class Wallet():
    def __init__(self, coin:Coin, reportData:ReportData, balance=0):
        # Coin in this wallet
        self.coin = coin

        # Dict of timestamp -> amount bought
        self.timestampBuys = {time:buy for time, buy in zip(reportData.buyData[coin.name]['Timestamp'].to_list(), reportData.buyData[coin.name]['Quantity Transacted'].to_list())}
        
        print(2)
        # Dict of timestamp -> amount bought
        self.timestampConverts = {time:-conv for time, conv in zip(reportData.convertData[coin.name]['Timestamp'].to_list(), reportData.convertData[coin.name]['Quantity Transacted'].to_list())}
        # Date -> cumlBalance dict (sparse)
        self.timestampCumlBalSparse = self.CalculateCumlBalanceSparse()
        # Date -> cumlBalance (filled)
        self.timestampCumlBalFilled = self.CalculateCumlBalanceFilled()
        # Coin total balance (latest)
        self.balance = list(self.timestampCumlBalSparse.values())[-1]

        # Create dash stats object and dump to json 
        self.dashStats = WalletDashStats(self)
        JSON_Str = json.dumps(self.dashStats.__dict__)
        # Save in public folder for accessing through react
        with open(r"D:/Coding/CryptoBalance/CryptoDashboardApp/public/Wallets/" + self.coin.symbol + r"_Wallet.JSON", 'w+') as f:
            json.dump(JSON_Str, f)
            

    # Calculate cumulative balance for buy/convert dates only
    def CalculateCumlBalanceSparse(self):
    
        buys = self.timestampBuys
        # Add converts to buys
        buys.update(self.timestampConverts)
        # Sort combined buy/convert by timestamp
        combinedSorted = {key:buys[key] for key in sorted(list(buys.keys()))}
        # Cumulative balance
        cumlBal = [sum(list(combinedSorted.values())[0:x:1]) for x in range(0, len(list(combinedSorted.values())))]
        
        # Return date -> cuml balance
        return {dt.strftime(time, '%Y-%m-%d'):cumlBal for time, cumlBal in zip(list(combinedSorted.keys()), cumlBal)}
    

    # Return dict with cuml balance on every date (for known price data)
    def CalculateCumlBalanceFilled(self):
        # All dates
        dates = list(self.coin.dateHighLow.keys())
        # First buy date
        startDate = list(self.timestampCumlBalSparse.keys())[-1]
        # Fill list of cuml balances
        cumlBalances = []
        lastValue = 0
        for date in dates:
            if date in self.timestampCumlBalSparse:
                lastValue = self.timestampCumlBalSparse[date]
                # Append the new cuml balance value
                cumlBalances.append(lastValue)
            else:
                # Append the previous cuml balance value
                cumlBalances.append(lastValue)
        
        return {date:bal for date, bal in zip(dates, cumlBalances)}
    

        
class WalletDashStats():
    def __init__(self, wallet:Wallet):
        self.coin = wallet.coin.name
        self.symbol = wallet.coin.symbol
        self.balance = wallet.balance 
        self.cumlBalancesSparse = wallet.timestampCumlBalSparse
        self.cumlBalancesFilled = wallet.timestampCumlBalFilled
        self.cumlBalancesUSDSparse = dict()
        self.cumlBalancesUSDSparse = {date:[FormatUSDPrice(self.cumlBalancesSparse[date] * price) for price in wallet.coin.dateHighLow[date]] for date in list(self.cumlBalancesSparse.keys())}
        self.cumlBalancesUSDFilled = {date:[FormatUSDPrice(self.cumlBalancesFilled[date] * price) for price in wallet.coin.dateHighLow[date]] for date in list(self.cumlBalancesFilled.keys())}
        


