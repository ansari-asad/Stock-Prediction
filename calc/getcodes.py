from nsetools import Nse

nse = Nse()

def getstocks():
	stocks = nse.get_stock_codes()
	stocks.pop('SYMBOL', None)
	return stocks

def verify(code):
	return nse.is_valid_code(code)