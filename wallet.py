
import datetime

from coinbaseReport import ReportData




class Coin():
    def __init__(self, name:str):
        # Name of the coin
        self.name = name
        # Year to date daily prices




class Wallet():
    def __init__(self, coin:Coin, reportData:ReportData, balance=0):
        # Coin in this wallet
        self.coin = coin
        
        # Coin balance
        self.balance = balance

        # Date -> cumlBalance dict 
        CalculateCumlBalances(reportData)
        


def CalculateCumlBalances(reportData:ReportData):
    for coin in reportData.currencies:
        buys = reportData.buyData[coin]['Quantity Transacted']
        converts = reportData.convertData[coin]['Quantity Transacted']
        combined = [buy - conv for buy,conv in zip(buys.to_list(), converts.to_list())]
        print(2)

