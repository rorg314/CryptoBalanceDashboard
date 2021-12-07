from coinbaseReport import *
from priceData import *
from plot import * 

def main(plot=False):
    print("Main")
    
    reportData = ReportData("./CoinbaseProcessing/Report.csv")
    
    currencies  = ['BTC', 'ETH', 'DOGE']
    pairs = [curr+"/USD" for curr in currencies]
    FetchCachedPriceData(pairs)
    
    coinWalletDict = dict()
    
    for currency in currencies:
        coin = Coin(currency)
        coinWalletDict[coin] = Wallet(coin, reportData)
    
    print("Stored wallet data")
    
    if(plot):
        labels = []
        fix, ax = plt.subplots()
        for currency in currencies:
            ax = PlotCumSpotPrice(reportData.buyData[currency], currency, ax=ax)
            ax = PlotActualCurrencyPrice(reportData.buyData[currency], currency, ax=ax)
            labels.append(f'{currency}$SPEND')
            labels.append(f'{currency}$WORTH')
        ax.legend(labels)
        plt.show()

    




if __name__ == "__main__":
    main()