from collections import defaultdict
from cryptocompare.cryptocompare import Timestamp
import pandas as pd
from matplotlib import pyplot as plt
from datetime import datetime as dt
import datetime
import json
from itertools import accumulate


CURRENCIES = ['BTC', 'ETH', 'DOGE']


# Build the dataframe from the report csv
def ExtractReportDataframe(reportPath):
    
    reportDataframe = pd.read_csv(reportPath)

    for col in reportDataframe.columns:
        if(isinstance(reportDataframe[col][0], str)):
            reportDataframe[col].str.lower()

    return DatetimeTimestamps(reportDataframe)


# Processing timestamp strings (YYYY-MM-DD T HH:MM:SS Z) into datetimes 
def DatetimeTimestamps(dataframe, dayOnly=False):
    timestampStrings = dataframe['Timestamp'].to_list()
    replace = ['T', 'Z', '-', ':']
    dateTimes = list()
    for time in timestampStrings:
        
        if(dayOnly):
            time = time.split('T')[0].replace('-', ' ')
            dateTimes.append(dt.strptime(time.strip(), '%Y %m %d'))
        else:
            for char in replace:
                time = time.replace(char, ' ')
            dateTimes.append(dt.strptime(time.strip(), '%Y %m %d %H %M %S'))
    
    dataframe.drop('Timestamp', axis=1, inplace=True)
    dataframe['Timestamp'] = dateTimes
    return dataframe


# Use to extract the buy/sell data for an individual currency
def ExtractCurrencyData(reportDf, currencyStr="BTC"):

    includeCols = ['Timestamp', 'Transaction Type', 'Quantity Transacted', 'Spot Price at Transaction', 'Subtotal',	'Total (inclusive of fees)', 'Fees', 'Notes']

    #Slice the dataframe by the asset and convert timestamps to datetimes (dates only)
    currencyDf = reportDf.loc[(reportDf['Asset'] == currencyStr)].loc[:, includeCols]

    # Slice by buy
    buyDf = currencyDf.loc[(currencyDf['Transaction Type'] == 'Buy')].loc[:, includeCols]

    # Slice by converts
    convertDf = currencyDf.loc[(currencyDf['Transaction Type'] == 'Convert') &(currencyDf['Fees'] > 0)].loc[:, includeCols]

    # # Extract amounts of converted currency from description col 
    # convertedToCurrencyDict = ExtractConvertData(convertDf, currencyStr)


    return currencyDf, buyDf, convertDf#, convertedToCurrencyDict


def ExtractConvertData(allConvertsDf:pd.DataFrame):
    # Dict with convertedToCurrency -> {timestamp:amount}
    convertedToCurrencyDict = defaultdict(lambda: defaultdict(float))

    timestamps = allConvertsDf['Timestamp'].to_list()
    notes = allConvertsDf['Notes'].to_list()

    for timestamp, note in zip(timestamps, notes):
        # Strip the note and split on spaces - last two elements are needed
        split = note.strip().split(' ')
        amount = float(split[-2])
        currency = split[-1]
        convertedToCurrencyDict[currency][timestamp] = convertedToCurrencyDict[currency][timestamp] + amount
    
    return convertedToCurrencyDict

    

#Filter the data to only include those columns 
def FilterCurrencyData(currencyDf, buyDf, convertDf):
    includeCols = ['Timestamp', 'Quantity Transacted', 'Spot Price at Transaction', 'Subtotal',	'Total (inclusive of fees)', 'Fees', 'Notes']

    return DatetimeTimestamps(currencyDf.loc[:, includeCols]), DatetimeTimestamps(buyDf.loc[:, includeCols]), DatetimeTimestamps(convertDf.loc[:, includeCols])


# Format a converted price in USD with 2 decimal places
def FormatUSD(rawPrice):
    return f"{rawPrice:.2f}"

def FormatBTC(raw):
    return f"{raw:.8f}"


# Process a pair of ordered lists of timestamps and transactions into a dict of timestamp -> transactions (accounts for transactions on the same day which it did not previously)
def TimestampTransactionsDict(timestamps:list, transactions:list):
    timestampTransactionsDict = defaultdict(list)
    
    for idx, timestamp in enumerate(timestamps):
        timestampTransactionsDict[timestamp].append(transactions[idx])
    
    return timestampTransactionsDict


# Same as above but aggregates multiple buys on single days
def TimestampTransactionsDayAggregate(timestamps:list, transactions:list):
    timestampTransactionsDict = dict()

    lastTimestamp = None

    for idx, timestamp in enumerate(timestamps):
        if(lastTimestamp == timestamp):
            # Add amount to day total
            timestampTransactionsDict[timestamp] = timestampTransactionsDict[timestamp] + transactions[idx]
        else:
            timestampTransactionsDict[timestamp] = transactions[idx]
        lastTimestamp = timestamp
    
    return timestampTransactionsDict
    

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
        



class ReportData():
    def __init__(self, reportPath="./CoinbaseProcessing/Report.csv"):
        self.reportDf = ExtractReportDataframe(reportPath)
        self.currencies = ['BTC', 'ETH', 'DOGE']
        
        # Build individual currency data from report dataframe
        self.currencyData, self.buyData, self.convertData, self.allConvertsDf = dict(), dict(), dict(), None
        for currency in self.currencies:
            self.currencyData[currency], self.buyData[currency], self.convertData[currency] = ExtractCurrencyData(self.reportDf, currency)
            if(self.allConvertsDf is None):
                # Create the initial all converts dataframe
                self.allConvertsDf = self.convertData[currency]
            else:
                #Update with any more converts
                self.allConvertsDf.update(self.convertData[currency])
        
        # Sort the allConverts by timestamp
        self.allConvertsDf.sort_values(by='Timestamp')
        
        # Extract all the converts

        self.convertedToCurrencyDict = ExtractConvertData(self.allConvertsDf)


        print(2)



class Wallet():
    def __init__(self, coin:Coin, reportData:ReportData):
        # Coin in this wallet
        self.coin = coin

        # Dict of timestamp -> amount bought
        self.timestampBuysDict = {time:trans for time, trans in zip(reportData.buyData[coin.name]['Timestamp'].to_list(), reportData.buyData[coin.name]['Quantity Transacted'].to_list())}
        
        # Dict of timestamp -> amount converted (sold - negative in base currency)
        self.timestampConvertSellsDict = {time:trans for time, trans in zip(reportData.convertData[coin.name]['Timestamp'].to_list(), [amt * -1 for amt in reportData.convertData[coin.name]['Quantity Transacted'].to_list()])}

        # Timestamp -> cumlBalance dict (sparse)
        self.timestampCumlBalSparse = self.TimestampCumlBalanceSparse()
        
        # Date -> cumlBalance (sparse)
        self.dateCumlBalSparse = self.DateStrCumlBalanceSparse()

        # Date -> cumlBalance (filled days)
        self.dateCumlBalFilled = self.DateCumlBalanceFilled()

        # Coin total balance (latest)
        self.balance = list(self.timestampCumlBalSparse.values())[-1]

        # Create dash stats object and dump to json 
        self.dashStats = WalletDashStats(self)
        JSON_Str = json.dumps(self.dashStats.__dict__)
        # Save in public folder for accessing through react
        with open(r"./CryptoDashboardApp/public/Wallets/" + self.coin.symbol + r"_Wallet.JSON", 'w+') as f:
            json.dump(JSON_Str, f)
            

    # Calculate cumulative balance for buy/convert dates only
    def TimestampCumlBalanceSparse(self):
    
        buys = self.timestampBuysDict
        # Add converts to buys
        buys.update(self.timestampConvertSellsDict)
        # Sort combined buy/convert by timestamp
        combinedSorted = {key:buys[key] for key in sorted(list(buys.keys()))}
        # Cumulative balance
        cumlBal = list(accumulate(list(combinedSorted.values())))

        # Return date -> cuml balance
        return {time:cumlBal for time, cumlBal in zip(list(combinedSorted.keys()), cumlBal)}

    # Aggregates cuml balance on single dates into dict of dateStr -> transacted amount
    def DateStrCumlBalanceSparse(self):
        
        cumlBalSparse = self.timestampCumlBalSparse
        
        dateStrCumlBalDict = dict()
        
        # Set start timestamp
        prevTimestamp = list(cumlBalSparse.keys())[0]
        prevDateStr = prevTimestamp._date_repr
        
        for timestamp in cumlBalSparse.keys():
            dateStr = timestamp._date_repr
            if(dateStr != prevDateStr):
                # Onto a new date, set cuml balance of the previous date 
                
                dateStrCumlBalDict[prevDateStr] = cumlBalSparse[prevTimestamp]
            prevDateStr = dateStr
            prevTimestamp = timestamp
        return dateStrCumlBalDict

    

    # Return dict with cuml balance on every date (for known price data)
    def DateCumlBalanceFilled(self):
        # All dates
        dates = list(self.coin.dateHighLow.keys())
        
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
        self.balance = FormatBTC(wallet.balance) 
        #self.timestampCumlBalSparse = wallet.timestampCumlBalSparse
        self.dateCumlBalSparse = wallet.dateCumlBalSparse
        self.dateCumlBalFilled = wallet.dateCumlBalFilled
        self.dateCumlBalUSDSparse = {date:[FormatUSD(self.dateCumlBalSparse[date] * price) for price in wallet.coin.dateHighLow[date]] for date in list(self.dateCumlBalSparse.keys())}
        self.cumlBalancesUSDFilled = {date:[FormatUSD(self.dateCumlBalFilled[date] * price) for price in wallet.coin.dateHighLow[date]] for date in list(self.dateCumlBalFilled.keys())}
        


