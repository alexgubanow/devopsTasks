#imports section
import json
import sys
import requests

#function return Ticker Data for EUR market for passed currency
#inputs are
#currency - name of currency for getting ticker data
#return JSON string with Ticker Data
def getTickerData(self, currency):
    #wrapped in try_catch
    try:
        #pushing http request to alphavantage with choosed currency and storing only json part of answer
        rq = requests.get('https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_DAILY&symbol='+
        currency +'&market=EUR&apikey=VEWJ1K6W3ENPI4NB').json()
    except:
        #Something went wrong
        print("Something went wrong")
    finally:
        try:
            #try to find time series array in json
            return rq['Time Series (Digital Currency Daily)']
        except:
            #return empty string if there isn't time series array
            return ''

#function return targeted tickers from input list
#inputs are
#tickers - source list of data
#target - behavior to match, could throw to 'pos' or 'neg'
def getSomeTickers(self, tickers, target):
    #temp array for matched tickers
    founded = []
    #avoid empty input array and wrong target input
    if tickers == [] or (target != 'pos' and target != 'neg'):
        #return empty array
        return founded
    #iterate over input array
    for ticker in tickers:
        #calc gain of current ticker
        tickerGain = float(tickers[ticker]['4a. close (EUR)']) - float(tickers[ticker]['1a. open (EUR)'])
        #compare calculated gain with target
        if (tickerGain > 0 and 'pos' == target) or (tickerGain < 0 and 'neg' == target):
            #push to ticker his timeStamp
            tickers[ticker]['timeStamp'] = ticker
            #push ticker to founded array
            founded.append(tickers[ticker])
    return founded

#getting BCH tickers
BCHtkrs = getTickerData(0, 'BCH')
#getting ETH tickers
ETHtkrs = getTickerData(0, 'ETH')
#getting LTC tickers
LTCtkrs = getTickerData(0, 'LTC')
#getting VOX tickers
VOXtkrs = getTickerData(0, 'VOX')

#avoid empty arrays
if BCHtkrs == '' or ETHtkrs == '' or LTCtkrs == '' or VOXtkrs == '':
    sys.exit("Don't have data to proccess")
#maybe for better performance filtering has to be done with storing what already sorted
#finding positive ends
BCHtkrsPos = getSomeTickers(0, BCHtkrs, 'pos')
ETHtkrsPos = getSomeTickers(0, ETHtkrs, 'pos')
LTCtkrsPos = getSomeTickers(0, LTCtkrs, 'pos')
VOXtkrsPos = getSomeTickers(0, VOXtkrs, 'pos')
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
for row in VOXtkrsPos:
    row['currency'] = 'VOX'
    positiveTickerData = positiveTickerData + str(row) + ','
positiveTickerData = positiveTickerData[:-1] + ']'
#replace char ' by "
positiveTickerData = positiveTickerData.replace("'", '"', -1)
#writing positive ends
f = open("positiveTickerData.txt", "w")
f.write(positiveTickerData)
f.close()

#finding negative ends
BCHtkrsNeg = getSomeTickers(0, BCHtkrs, 'neg')
ETHtkrsNeg = getSomeTickers(0, ETHtkrs, 'neg')
LTCtkrsNeg = getSomeTickers(0, LTCtkrs, 'neg')
VOXtkrsNeg = getSomeTickers(0, VOXtkrs, 'neg')
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
for row in VOXtkrsNeg:
    row['currency'] = 'VOX'
    negativeTickerData = negativeTickerData + str(row) + ','
negativeTickerData = negativeTickerData[:-1] + ']'
#replace char ' by "
negativeTickerData = negativeTickerData.replace("'", '"', -1)
#writing negative ends
f = open("negativeTickerData.txt", "w")
f.write(negativeTickerData)
f.close()