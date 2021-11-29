from coinbaseReport import *
from wallet import *
from plot import * 
def main():
    print("Main")

    reportData = ReportData("./Report.csv")
    currencies  = ['BTC', 'ETH', 'DOGE']
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