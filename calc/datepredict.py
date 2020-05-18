#imports
from math import *
from nsepy import get_history
from datetime import date,timedelta
from dateutil.relativedelta import relativedelta
import numpy as np

#Collect stock data
def getdates(stock):
    data = get_history(symbol=stock,
                        start=date.today() - relativedelta(months=+1), 
                        end=date.today())    #specified date

    retdata = dict()
    #determining the high and low of the month with date
    data = data.reset_index()
    data=data[['Date','Open','High','Low','Close']]
    index_high=data['High'].idxmax()
    index_low=data['Low'].idxmin()
    high_date=data.loc[ index_high , : ]['Date']
    low_date=data.loc[ index_low , : ]['Date']
    retdata['High'] = max(data['High'])
    retdata['highDate'] = str(high_date)
    retdata['Low'] = min(data['Low'])
    retdata['lowDate'] = str(low_date)
    retdata['Close'] = data['Close'][len(data)-1]

    price_diff=max(data['High'])-min(data['Low'])

    #degree conversion
    degree=((sqrt(price_diff)*180)-225)%360

    #calculating number having same degree
    n=3
    l=[]
    for i in range(1,n):
        #l.append(round((2*i+2*degree/360-1.25)**2))
        l.append(round((2*i+2*degree/360+1.25)**2))

    #Predicting future date (low/high)
    preddate=[]
    for i in l:
        preddate.append(high_date + relativedelta(days=+i))
        preddate.append(low_date + relativedelta(days=+i))

    retdata['predictedDates'] = []
    for i in preddate:
        if not np.is_busday(i):
            #print(i,"Not a Business day")
            d = i
            next = d + timedelta(days= 7-d.weekday() if d.weekday()>3 else 1)
            retdata['predictedDates'] = retdata['predictedDates'] + [str(next)]
        else:
            retdata['predictedDates'] = retdata['predictedDates'] + [str(i)]
    return retdata