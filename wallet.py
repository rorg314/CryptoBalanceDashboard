
import datetime




class Coin():
    def __init__(self, name:str):
        # Name of the coin
        self.name = name



class Wallet():
    def __init__(self, coin:Coin):
        # Coin in this wallet
        self.coin = coin
        
        # datetime -> coin balance dict
        self.timeCoinBalanceDict = dict()

        # datetime -> bought amount in GBP
        self.timeBoughtAmountDict = dict()


    