from cryptocompare.cryptocompare import Timestamp
import pandas as pd
from matplotlib import pyplot as plt
import cryptocompare
from datetime import datetime
from time import mktime




# Build the dataframe from the report csv
def ExtractBalanceDataframe(reportPath):
    
    reportDataframe = pd.read_csv(reportPath)

    for col in reportDataframe.columns:
        if(isinstance(reportDataframe[col][0], str)):
            reportDataframe[col].str.lower()

    return reportDataframe


def DatetimeTimestamps(dataframe):
    raw = dataframe['Timestamp'].to_list()
    dateTimes = list()
    for time in raw:
        time = time.split('T')[0].replace('-', ' ').strip()
        dateTimes.append(datetime.strptime(time, '%Y %m %d'))
    
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
    convertDf = currencyDf.loc[(currencyDf['Transaction Type'] == 'Convert')]

    return FilterCurrencyData(currencyDf, buyDf, convertDf)



# Filter the data to only include those columns 
def FilterCurrencyData(currencyDf, buyDf, convertDf):
    includeCols = ['Timestamp', 'Quantity Transacted', 'Spot Price at Transaction', 'Subtotal',	'Total (inclusive of fees)']
    return DatetimeTimestamps(currencyDf.loc[:, includeCols]), DatetimeTimestamps(buyDf.loc[:, includeCols]), DatetimeTimestamps(convertDf.loc[:, includeCols])


# ======================================================== #
# ======================== CLASSES ======================= #
# ======================================================== #


class Coin():
    def __init__(self, name:str):
        # Name of the coin
        self.name = name
        # Year to date daily prices


class ReportData():
    def __init__(self, reportPath="./Report.csv"):
        self.reportDf = ExtractBalanceDataframe(reportPath)
        self.currencies = ['BTC', 'ETH', 'DOGE']
        
        # Build individual currency data from report dataframe
        self.currencyData, self.buyData, self.convertData = dict(), dict(), dict()
        for currency in self.currencies:
            self.currencyData[currency], self.buyData[currency], self.convertData[currency] = ExtractCurrencyData(self.reportDf, currency)

        for coin in self.currencies:
            Wallet(coin, self)
        

class Wallet():
    def __init__(self, coin:Coin, reportData:ReportData, balance=0):
        # Coin in this wallet
        self.coin = coin
        
        # Coin balance
        self.balance = balance

        # Dict of timestamp -> amount bought
        self.timestampBuys = {time:buy for time, buy in zip(reportData.buyData[coin]['Timestamp'].to_list(), reportData.buyData[coin]['Quantity Transacted'].to_list())}
        # Dict of timestamp -> amount bought
        self.timestampConverts = {time:-conv for time, conv in zip(reportData.convertData[coin]['Timestamp'].to_list(), reportData.convertData[coin]['Quantity Transacted'].to_list())}
        
        # Date -> cumlBalance dict 
        self.timestampCumlBal = self.CalculateCumlBalance()

        
        
    # Calculate cumulative bal for buy/convert
    def CalculateCumlBalance(self):
    
        buys = self.timestampBuys
        # Add converts to buys
        buys.update(self.timestampConverts)
        # Sort combined buy/convert by timestamp
        combinedSorted = {key:buys[key] for key in sorted(list(buys.keys()))}
        
        cumlBal = [sum(list(combinedSorted.values())[0:x:1]) for x in range(0, len(list(combinedSorted.values())))]

        return {time:cumlBal for time, cumlBal in zip(list(combinedSorted.keys()), cumlBal)}

        


        


