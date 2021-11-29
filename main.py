from coinbaseReport import *
from wallet import *
from plot import * 
def main():
    print("Main")

    reportData = ReportData("./Report.csv")

    fix, ax = plt.subplots()
    ax = PlotCumSpotPrice(reportData.buyData['BTC'], 'BTC', ax=ax)
    ax = PlotActualCurrencyPrice(reportData.buyData['BTC'], 'BTC', ax=ax)
    plt.show()




if __name__ == "__main__":
    main()