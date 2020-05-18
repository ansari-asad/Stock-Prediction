from django.shortcuts import render
from django.http import HttpResponse

from . import getcodes, history, datepredict, wave
# Create your views here.
def home(request):
	return render(request, 'home.html.j2', {'stocks': getcodes.getstocks()})

def stock(request):
	code = request.GET['stockcode'].split()[0]
	code = code.upper()
	history.getcandlestick(code)
	d = {'stock':code, 'stocks': getcodes.getstocks()}
	d.update(datepredict.getdates(code))
	d.update(wave.elliott(code, d['Low'], d['High'], d['Close'], d['lowDate'], d['highDate']))
	if getcodes.verify(code):
		return render(request, 'result.html.j2', d)
	else:
		return HttpResponse("<script>alert('Invalid Stock Name!');location.replace('/')</script>")