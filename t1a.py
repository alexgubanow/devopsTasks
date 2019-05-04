#imports section
import requests

#function return Ticker Data for EUR market for passed currency
def getTickerData(self, currency):
    return requests.get('https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_DAILY&symbol='+
    currency +'&market=EUR&apikey=VEWJ1K6W3ENPI4NB')

#getting BCH tickers
BCHrq = getTickerData(0, 'BCH')
#getting ETH tickers
ETHrq = getTickerData(0, 'ETH')
#getting LTC tickers
LTCrq = getTickerData(0, 'LTC')

#finding positive ends


print(ETHrq.json())