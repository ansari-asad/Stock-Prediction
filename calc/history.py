#imports
from nsepy import get_history
from datetime import date
from dateutil.relativedelta import relativedelta
import matplotlib.pyplot as plt
from mpl_finance import candlestick_ohlc
import pandas as pd
import matplotlib.dates as mpl_dates
import numpy as np
plt.rcParams['figure.figsize'] = 10, 5

#Collecting OHLC stock data 
def getcandlestick(stock):
	data = get_history(symbol=stock,
                    	start=date.today() - relativedelta(months=+3), 
                    	end=date.today())

	data = data.reset_index()
	data=data[['Date','Open','High','Low','Close']]

	#visualization
	plt.style.use('ggplot')
	ohlc=data
	ohlc['Date'] = pd.to_datetime(ohlc['Date'])
	ohlc['Date'] = ohlc['Date'].apply(mpl_dates.date2num)
	ohlc = ohlc.astype(float)
	fig, ax = plt.subplots()
	candlestick_ohlc(ax, ohlc.values, width=0.6, colorup='green', colordown='red', alpha=0.8)

	# Setting labels & titles
	ax.set_xlabel('Date')
	ax.set_ylabel('Price')
	fig.suptitle('Daily Candlestick Chart of '+stock)

	# Formatting Date
	date_format = mpl_dates.DateFormatter('%d-%m-%Y')
	ax.xaxis.set_major_formatter(date_format)
	fig.autofmt_xdate()
	fig.tight_layout()

	#mean
	#ohlc['SMA5'] = ohlc["Close"].rolling(5).mean()
	#ax.plot(ohlc['Date'], ohlc['SMA5'], color = 'green', label = 'SMA5')
	plt.savefig('./media/candlestick.png', dpi=100, bbox_inches='tight')