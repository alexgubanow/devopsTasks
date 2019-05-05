#imports section
import json
import sys
import requests

#function return Ticker Data for EUR market for passed currency
#inputs are
#currency - name of currency for getting ticker data
#return JSON string with Ticker Data
def getTickerData(self, currency):
    try:
        rq = requests.get('https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_DAILY&symbol='+
        currency +'&market=EUR&apikey=VEWJ1K6W3ENPI4NB').json()
    except:
        print("Something went wrong")
    finally:
        try:
            return rq['Time Series (Digital Currency Daily)']
        except:
            return ''

#function return targeted tickers from input list
#inputs are
#tickers - source list of data
#target - behavior to match, could throw to 'pos' or 'neg'
def getSomeTickers(self, tickers, target):
    founded = []
    if tickers == [] or (target != 'pos' and target != 'neg'):
        return founded
    for ticker in tickers:
        tickerGain = float(tickers[ticker]['4a. close (EUR)']) - float(tickers[ticker]['1a. open (EUR)'])
        if (tickerGain > 0 and 'pos' == target) or (tickerGain < 0 and 'neg' == target):
            tickers[ticker]['timeStamp'] = ticker
            founded.append(tickers[ticker])
    return founded

#getting BCH tickers
BCHtkrs = getTickerData(0, 'BCH')
#getting ETH tickers
ETHtkrs = getTickerData(0, 'ETH')
#getting LTC tickers
LTCtkrs = getTickerData(0, 'LTC')
if BCHtkrs == '' or ETHtkrs == '' or LTCtkrs == '':
    sys.exit("Don't have data to proccess")

#finding positive ends
BCHtkrsPos = getSomeTickers(0, BCHtkrs, 'pos')
ETHtkrsPos = getSomeTickers(0, ETHtkrs, 'pos')
LTCtkrsPos = getSomeTickers(0, LTCtkrs, 'pos')
#adding currency mark to each row and put all in one by JSON way
positiveTickerData = '['
for row in BCHtkrsPos:
    row['currency'] = 'BCH'
    positiveTickerData = positiveTickerData + str(row) + ','
for row in ETHtkrsPos:
    row['currency'] = 'ETH'
    positiveTickerData = positiveTickerData + str(row) + ','
for row in LTCtkrsPos:
    row['currency'] = 'LTC'
    positiveTickerData = positiveTickerData + str(row) + ','
positiveTickerData = positiveTickerData[:-1] + ']'
#writing positive ends
f = open("positiveTickerData.txt", "w")
f.write(positiveTickerData)
f.close()

#finding negative ends
BCHtkrsNeg = getSomeTickers(0, BCHtkrs, 'neg')
ETHtkrsNeg = getSomeTickers(0, ETHtkrs, 'neg')
LTCtkrsNeg = getSomeTickers(0, LTCtkrs, 'neg')
#adding currency mark to each row and put all in one by JSON way
negativeTickerData = '['
for row in BCHtkrsNeg:
    row['currency'] = 'BCH'
    negativeTickerData = negativeTickerData + str(row) + ','
for row in ETHtkrsNeg:
    row['currency'] = 'ETH'
    negativeTickerData = negativeTickerData + str(row) + ','
for row in LTCtkrsNeg:
    row['currency'] = 'LTC'
    negativeTickerData = negativeTickerData + str(row) + ','
negativeTickerData = negativeTickerData[:-1] + ']'
#writing negative ends
f = open("negativeTickerData.txt", "w")
f.write(negativeTickerData)
f.close()