from coinbaseReport import *
from priceData import *
from plot import * 

from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/GetWalletData')
def index(plot=False):
    print("Main")
    
    reportData = ReportData("./CoinbaseProcessing/Report.csv")
    
    
    pairs = [curr+"/USD" for curr in CURRENCIES]
    FetchCachedPriceData(pairs)
    
    coinWalletDict = dict()
    
    for currency in CURRENCIES:
        coin = Coin(currency)
        coinWalletDict[coin] = Wallet(coin, reportData)
    
    responseDict = {coin.name:wallet.walletJson for coin, wallet in zip(coinWalletDict.keys(), coinWalletDict.values())}
    
    print("Stored wallet data")

    if(plot):
        Plot(reportData)

    response = jsonify(responseDict)
    response.headers.add('Access-Control-Allow-Origin', '*')
    
    return response


    
def Plot(reportData):
    
    labels = []
    fix, ax = plt.subplots()
    for currency in CURRENCIES:
        ax = PlotCumSpotPrice(reportData.buyData[currency], currency, ax=ax)
        ax = PlotActualCurrencyPrice(reportData.buyData[currency], currency, ax=ax)
        labels.append(f'{currency}$SPEND')
        labels.append(f'{currency}$WORTH')
    ax.legend(labels)
    plt.show()


if __name__ == "__main__":
    app.run(debug=True)