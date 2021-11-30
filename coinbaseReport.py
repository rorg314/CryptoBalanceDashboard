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

    # Slice by buy/sells
    buyDf = currencyDf.loc[(currencyDf['Transaction Type'] == 'Buy')]

    # Slice by converts
    convertDf = currencyDf.loc[(currencyDf['Transaction Type'] == 'Convert')]

    return FilterCurrencyData(currencyDf, buyDf, convertDf)



# Filter the data to only include those columns 
def FilterCurrencyData(currencyDf, buyDf, convertDf):
    includeCols = ['Timestamp', 'Quantity Transacted', 'Spot Price at Transaction', 'Subtotal',	'Total (inclusive of fees)']
    return DatetimeTimestamps(currencyDf.loc[:, includeCols]), DatetimeTimestamps(buyDf.loc[:, includeCols]), DatetimeTimestamps(convertDf.loc[:, includeCols])



class ReportData():
    def __init__(self, reportPath="./Report.csv"):
        self.reportDf = ExtractBalanceDataframe(reportPath)
        self.currencies = ['BTC', 'ETH', 'DOGE']
        
        # Build individual currency data from report dataframe
        self.currencyData, self.buyData, self.convertData = dict(), dict(), dict()
        for currency in self.currencies:
            self.currencyData[currency], self.buyData[currency], self.convertData[currency] = ExtractCurrencyData(self.reportDf, currency)
        
        # Currency -> total held dict
        


