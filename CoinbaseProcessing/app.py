from coinbaseReport import *
from priceData import *
from plot import * 

from flask import Flask, jsonify

app = Flask(__name__)

from config import ROOTPATH


@app.route('/GetWalletData')
def index(plot=False):
    print("Main")
    
    # Fetch price data 
    pairs = [curr+"/USD" for curr in CURRENCIES]
    FetchCachedPriceData(pairs)

    reportData = ReportData(reportPath=ROOTPATH + "/CoinbaseProcessing/Report.csv")
    
    responseDict = {coin.name:wallet.dashStats.__dict__ for coin, wallet in zip(reportData.coinWalletDict.keys(), reportData.coinWalletDict.values())}
    
    print("Stored wallet data")

    # if(plot):
    #     Plot(reportData)

    response = jsonify(responseDict)
    response.headers.add('Access-Control-Allow-Origin', '*')
    
    return response


    
# def Plot(reportData):
    
#     labels = []
#     fix, ax = plt.subplots()
#     for currency in CURRENCIES:
#         ax = PlotCumSpotPrice(reportData.buyData[currency], currency, ax=ax)
#         ax = PlotActualCurrencyPrice(reportData.buyData[currency], currency, ax=ax)
#         labels.append(f'{currency}$SPEND')
#         labels.append(f'{currency}$WORTH')
#     ax.legend(labels)
#     plt.show()


if __name__ == "__main__":
    app.run(debug=True)