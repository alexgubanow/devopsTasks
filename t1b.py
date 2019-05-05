#imports section
import json
import sys

#fuction to calc gain of stock
def getGain(self, stock):
    return float(stock['4a. close (EUR)']) - float(stock['1a. open (EUR)'])

#function looking for target gain in array of tickers
#inputs are
#tickers - array with stocks
#target - desired gain, could be 'MAX' or 'MIN'
def getExtremGain(self, tickers, target):
    targetGain = 0
    targetTicker = []
    #avoid empty input
    if tickers == []:
        return targetTicker
    #iterate over given tickers array
    for p in tickers:
        #compare it to lastest gain
        if (getGain(0, p) > targetGain and target == 'MAX') or (getGain(0, p) < targetGain and target == 'MIN'):
            targetTicker = p
            targetGain = getGain(0, p)
    return targetTicker

#opening positive gains
with open('positiveTickerData.txt') as positiveTickerData:
    try:
        #try to decode json string
        data = json.load(positiveTickerData)
    except:
        print('No JSON in given file')
    finally:
        #get biggest gain
        biggestGain = getExtremGain(0, data, 'MAX')
print('biggest gain has this record:\n ' + str(biggestGain))
print('')
    
#opening negative gains
with open('negativeTickerData.txt') as negativeTickerData:
    try:
        #try to decode json string
        data = json.load(negativeTickerData)
    except:
        print('No JSON in given file')
    finally:
        #get biggest loss
        biggestLoss = getExtremGain(0, data, 'MIN')
print('biggest loss has this record:\n ' + str(biggestLoss))