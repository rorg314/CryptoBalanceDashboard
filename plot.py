
from coinbaseReport import *

# Plot all buys
def PlotBuys(reportData:ReportData, currency:str, ax=None):
    buyData = reportData.buyData[currency]

    timestamps = [mktime(time.timetuple()) for time in buyData['Timestamp']]
    buyUSD = buyData['Total (inclusive of fees)']

    if(not ax):
        fix, ax = plt.subplots()
        ax.plot(timestamps, buyUSD)
        plt.show()
    else:
        ax.plot(timestamps, buyUSD)
        return ax


# Cumulative price over time (spot price)
def PlotCumSpotPrice(priceData, currency:str, ax=None):

    timestamps = [mktime(time.timetuple()) for time in priceData['Timestamp']]
    buyUSD = priceData['Total (inclusive of fees)'].to_list()
    cumUSD = [sum(buyUSD[0:x:1]) for x in range(0, len(buyUSD))]

    if(not ax):
        fix, ax = plt.subplots()
        ax.plot(timestamps, cumUSD)
        plt.show()
    else:
        ax.plot(timestamps, cumUSD)
        return ax


# Plot actual daily price of asset balance 
def PlotActualCurrencyPrice(priceData, currency:str, ax=None):
    
    unixTimes = [mktime(time.timetuple()) for time in priceData['Timestamp']]
            
    amounts = priceData['Quantity Transacted'].to_list()
    cumAmount = [sum(amounts[0:x:1]) for x in range(0, len(amounts))]

    realSpotPrices = [cryptocompare.get_historical_price(currency, 'USD', time)[currency]['USD'] for time in unixTimes]
    realPrices = [a*b for a, b in zip(cumAmount, realSpotPrices)]
    
    if(not ax):
        fix, ax = plt.subplots()
        ax.plot(unixTimes, realPrices)
        plt.show()
    else:
        ax.plot(unixTimes, realPrices)
        return ax

