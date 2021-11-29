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


def UnixTimestamp(dataframe):
    raw = dataframe['Timestamp'].to_list()
    unixTimes = list()
    for time in raw:
        time = time.split('T')[0].replace('-', ' ').strip()
        unixTimes.append(mktime(datetime.strptime(time, '%Y %m %d').timetuple()))
    
    dataframe.drop('Timestamp', axis=1, inplace=True)
    dataframe['Timestamp'] = unixTimes
    return dataframe

# Use to extract the buy/sell data for an individual currency
def ExtractCurrencyData(reportDf, currencyStr="BTC"):

    assetList = reportDf['Asset']

    #Slice the dataframe by the asset 
    currencyDf = reportDf.loc[(reportDf['Asset'] == currencyStr)]

    # Slice by buy/sells
    buyDf = currencyDf.loc[(currencyDf['Transaction Type'] == 'Buy')]

    # Slice by converts
    convertDf = currencyDf.loc[(currencyDf['Transaction Type'] == 'Convert')]

    return FilterCurrencyData(currencyDf, buyDf, convertDf)



# Filter the data to only include those columns 
def FilterCurrencyData(currencyDf, buyDf, convertDf):
    includeCols = ['Timestamp', 'Quantity Transacted', 'Spot Price at Transaction', 'Subtotal',	'Total (inclusive of fees)']
    return UnixTimestamp(currencyDf.loc[:, includeCols]), UnixTimestamp(buyDf.loc[:, includeCols]), UnixTimestamp(convertDf.loc[:, includeCols])




class ReportData():
    def __init__(self, reportPath="./Report.csv"):
        self.reportDf = ExtractBalanceDataframe(reportPath)
        self.currencies = ['BTC', 'ETH', 'DOGE']
        
        # Build individual currency data from report dataframe
        self.currencyData, self.buyData, self.convertData = dict(), dict(), dict()
        for currency in self.currencies:
            self.currencyData[currency], self.buyData[currency], self.convertData[currency] = ExtractCurrencyData(self.reportDf, currency)
        
        fix, ax = plt.subplots()
        ax = PlotCumSpotPrice(self.buyData['BTC'], 'BTC', ax=ax)
        ax = PlotActualCurrencyPrice(self.buyData['BTC'], 'BTC', ax=ax)
        plt.show()
        print(2)


# Plot all buys
def PlotBuys(reportData:ReportData, currency:str, ax=None):
    buyData = reportData.buyData[currency]

    timestamps = buyData['Timestamp']
    buyUSD = buyData['Total (inclusive of fees)']

    if(not ax):
        fix, ax = plt.subplots()
        ax.plot(timestamps, buyUSD)
        plt.show()
    else:
        ax.plot(timestamps, buyUSD)
        return ax

# Cumulative price over time (spot price)
def PlotCumSpotPrice(priceData, currency:str, ax=None):

    timestamps = priceData['Timestamp']
    buyUSD = priceData['Total (inclusive of fees)'].to_list()
    cumUSD = [sum(buyUSD[0:x:1]) for x in range(0, len(buyUSD))]

    if(not ax):
        fix, ax = plt.subplots()
        ax.plot(timestamps, cumUSD)
        plt.show()
    else:
        ax.plot(timestamps, cumUSD)
        return ax

def PlotActualCurrencyPrice(priceData, currency:str, ax=None):
    
    unixTimes = priceData['Timestamp']
            
    amounts = priceData['Quantity Transacted'].to_list()
    cumAmount = [sum(amounts[0:x:1]) for x in range(0, len(amounts))]

    realSpotPrices = [cryptocompare.get_historical_price(currency, 'USD', time)[currency]['USD'] for time in unixTimes]
    realPrices = [a*b for a, b in zip(cumAmount,realSpotPrices)]
    
    if(not ax):
        fix, ax = plt.subplots()
        ax.plot(unixTimes, realPrices)
        plt.show()
    else:
        ax.plot(unixTimes, realPrices)
        return ax

