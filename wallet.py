
import datetime








class Wallet():
    def __init__(self, coin:str):
        # Name of the coin in this wallet
        self.coin = coin

        # datetime -> coin balance dict
        self.timeCoinBalanceDict = dict()

        # datetime -> bought amount in GBP
        self.timeBoughtAmountDict = dict()