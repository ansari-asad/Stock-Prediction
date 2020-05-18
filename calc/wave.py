#imports
from math import *
from nsepy import get_history
from datetime import date, timedelta, datetime
from dateutil.relativedelta import relativedelta
import numpy as np

#Collect stock data
def uptrend(LowPrice, HighPrice):
    Wave1StartPoint = LowPrice
    Wave1EndPoint = HighPrice
    Wave2StartPoint = Wave1EndPoint
    Wave2EndPoint = Wave2StartPoint - ((HighPrice - LowPrice) * 0.618)
    Wave3StartPoint = Wave2EndPoint 
    Wave3EndPoint = Wave3StartPoint + ((HighPrice - LowPrice) * 1.618)
    Wave4StartPoint = Wave3EndPoint
    Wave4EndPoint = Wave4StartPoint - ((Wave3EndPoint - Wave3StartPoint) * 0.382)
    Wave5StartPoint = Wave4EndPoint
    Wave5EndPoint = Wave5StartPoint + (HighPrice - LowPrice)  
    WaveAStartPoint = Wave5EndPoint
    WaveAEndPoint = WaveAStartPoint - ((Wave5EndPoint - Wave5StartPoint) * 0.382)
    WaveBStartPoint = WaveAEndPoint
    WaveBEndPoint = WaveBStartPoint + (((Wave5EndPoint - Wave5StartPoint) * 0.382) * 0.618)
    WaveCStartPoint = WaveBEndPoint
    WaveCEndPoint = WaveCStartPoint - ((Wave5EndPoint - Wave5StartPoint) * 0.382)
    points=[Wave1StartPoint, Wave1EndPoint, Wave2EndPoint,
       Wave3EndPoint, Wave4EndPoint, Wave5EndPoint, WaveAEndPoint, WaveBEndPoint, WaveCEndPoint]
    return points

def downtrend(LowPrice, HighPrice):
    Wave1StartPoint = HighPrice
    Wave1EndPoint = LowPrice
    Wave2StartPoint = Wave1EndPoint
    Wave2EndPoint = Wave1EndPoint + ((Wave1StartPoint - Wave1EndPoint) * 0.618)
    Wave3StartPoint = Wave2EndPoint
    Wave3EndPoint = Wave2EndPoint - ((Wave1StartPoint - Wave1EndPoint) * 1.618)
    Wave4StartPoint = Wave3EndPoint
    Wave4EndPoint = Wave3EndPoint + (((Wave1StartPoint - Wave1EndPoint) * 1.618) * 0.382)
    Wave5StartPoint = Wave4EndPoint
    Wave5EndPoint = Wave4EndPoint - (Wave1StartPoint - Wave1EndPoint)
    WaveAStartPoint = Wave5EndPoint
    WaveAEndPoint = Wave5EndPoint + ((Wave1StartPoint - Wave1EndPoint) * 0.382)
    WaveBStartPoint = WaveAEndPoint
    WaveBEndPoint = WaveAEndPoint - (((Wave1StartPoint - Wave1EndPoint) * 0.382) * 0.618)
    WaveCStartPoint = WaveBEndPoint
    WaveCEndPoint = WaveBEndPoint + ((Wave1StartPoint - Wave1EndPoint) * 0.382)
    points=[Wave1StartPoint, Wave1EndPoint, Wave2EndPoint,
       Wave3EndPoint, Wave4EndPoint, Wave5EndPoint, WaveAEndPoint, WaveBEndPoint, WaveCEndPoint]
    return points

def elliott(stock, LowPrice, HighPrice, ClosePrice, low_date, high_date):
    low_date = datetime.strptime(low_date, '%Y-%m-%d').date()
    high_date = datetime.strptime(high_date, '%Y-%m-%d').date()
    if ClosePrice < HighPrice:
        print('downtrend')
        points=downtrend(LowPrice, HighPrice)
    else:
        print('uptrend')
        points=uptrend(LowPrice, HighPrice)
    elliottwave = dict()
    points = [round(i) for i in points]
    elliottwave['elliottPrices'] = points

    #degree conversion
    for k in range(0,len(points)-1):
        price_diff=abs(points[k]-points[k+1])
        degree=((sqrt(price_diff)*180)-225)%360
        #calculating number having same degree
        l=[]
        for i in range(1,3):
            #l.append(round((2*i+2*degree/360-1.25)**2))
            l.append(round((2*i+2*degree/360+1.25)**2))
        elliottwave['Wave '+str(k+1)] = []
        #Predicting future date (low/high)
        preddate=[]
        for j in l:
            preddate.append(high_date+ relativedelta(days=+j))
            preddate.append(low_date+ relativedelta(days=+j))
        for a in preddate:
            elliottwave['Wave '+str(k+1)] = elliottwave['Wave '+str(k+1)] + [str(a)]
    return elliottwave
