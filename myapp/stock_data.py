from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings 
import pymysql
import json 
import bs4
import requests
from bs4 import BeautifulSoup 
from . import hreflist as hf
from . import data
from bsedata.bse import BSE



def getcmp(request,ticker):        #this function returns cmp of ticker
	try:
		url = requests.get("https://finance.yahoo.com/quote/{0}?p={0}".format(ticker), timeout=2)
		soup = bs4.BeautifulSoup(url.text, features="html.parser")
		price = soup.find_all("div", {'class': 'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find('span').text
		price=price.replace(',','')
		return HttpResponse(price)
	except requests.Timeout as e:
		pass
	else:
		pass
	finally:
		pass


def updateStockInfo(request):		#this function retuurns cmp,chng,pchng... of ticker
	ticker = str(request.GET.get('ticker', None))
	if ".NS" not in ticker:
		ticker = hf.codes[ticker][0] + ".NS"
	try:
		prices = []
		url = requests.get("https://finance.yahoo.com/quote/{0}?p={0}".format(ticker), timeout=3)
		soup = bs4.BeautifulSoup(url.text, features="html.parser")
		res1 = soup.find_all("div", {'class': 'My(6px) Pos(r) smartphone_Mt(6px)'})
		price = res1[0].find('span').text
		price=price.replace(',','')
		chngline = res1[0].find('span', {'data-reactid': '33'}).text
		chng,pchng = chngline.split('(')
		pchng = pchng.replace(")","")
		res = soup.find_all("td", {'class': 'Ta(end) Fw(600) Lh(14px)'})
		openp = res[0].find('span').text
		close = res[1].find('span').text
		lowhigh = res[4].text
		lowhigh52 = res[5].text
		volume = res[6].find('span').text
		mcap = res[8].find('span').text
		prices = [price, chng, pchng, openp, close, lowhigh, lowhigh52, volume, mcap]
		print("NSE")
		return HttpResponse(json.dumps(prices))

	except Exception as e:
		b = BSE()
		code = hf.bsecode[ticker]
		q = b.getQuote(str(code))
		price = q['currentValue']
		price=price.replace(',','')
		chng = q['change']
		pchng = q['pChange']
		openp = q['previousOpen']
		close = q['previousClose']
		lowhigh = q['dayLow'] + ' - ' + q['dayHigh']
		lowhigh52 = q['52weekLow'] + ' - ' + q['52weekHigh']
		volume = q['totalTradedQuantity']
		mcap = q['marketCapFull']
		prices=[]
		prices = [price, chng, pchng, openp, close, lowhigh, lowhigh52, volume, mcap]
		print("BSE")
		return HttpResponse(json.dumps(prices))	

	except:
		return HttpResponse(json.dumps("True"))
	


def updateshownifty50(request):
    # url = requests.get(
    #     'https://www.moneycontrol.com/stocks/marketstats/indexcomp.php?optex=NSE&opttopic=indexcomp&index=9')
    # soup = bs4.BeautifulSoup(url.text, features="html.parser")
    # tickers = []
    # i = 0
    # pricel=[]
    # chngl=[]
    # pchngl=[]
    # y = ['ADANIPORTS.NS', 'ASIANPAINT.NS', 'AXISBANK.NS', 'BAJAJ-AUTO.NS', 'BAJAJFINSV.NS', 'BAJFINANCE.NS', 'BHARTIARTL.NS', 'BPCL.NS', 'BRITANNIA.NS', 'CIPLA.NS', 'COALINDIA.NS', 'DIVISLAB.NS', 'DRREDDY.NS', 'EICHERMOT.NS', 'GAIL.NS', 'GRASIM.NS', 'HCLTECH.NS', 'HDFC.NS', 'HDFCBANK.NS', 'HDFCLIFE.NS', 'HEROMOTOCO.NS', 'HINDALCO.NS', 'HINDUNILVR.NS', 'ICICIBANK.NS', 'INDUSINDBK.NS', 'INFY.NS', 'IOC.NS', 'ITC.NS', 'JSWSTEEL.NS', 'KOTAKBANK.NS', 'LT.NS', 'M&M.NS', 'MARUTI.NS', 'NESTLEIND.NS', 'NTPC.NS', 'ONGC.NS', 'POWERGRID.NS', 'RELIANCE.NS', 'SBILIFE.NS', 'SBIN.NS', 'SHREECEM.NS', 'SUNPHARMA.NS', 'TATAMOTORS.NS', 'TATASTEEL.NS', 'TCS.NS', 'TECHM.NS', 'TITAN.NS', 'ULTRACEMCO.NS', 'UPL.NS', 'WIPRO.NS']
    # while (i < 200):
    # 	price = soup.find_all("td", {'align': 'right'})[i].text
    # 	price=price.replace(',','')
    # 	chng = soup.find_all("td", {'align': 'right'})[i + 1].text
    # 	pchng = soup.find_all("td", {'align': 'right'})[i + 2].text
    # 	pricel.append(price)
    # 	chngl.append(chng)
    # 	pchngl.append(pchng)
    # 	i += 4
    # data = {"price":pricel, "chng": chngl, "pchng":pchngl} 
    return HttpResponse(json.dumps(data.nifty50data))


def updatecmp(request):			#this function updates cmps in db
	conn = pymysql.connect( host='localhost',	port =3306 , user='root',  password = "123",   db='pgrdb' ) 
	cur = conn.cursor()
	cur.execute("SELECT company from STOCKS")
	conn.commit()
	companies = cur.fetchall()
	for company in companies:
		url = requests.get('https://finance.yahoo.com/quote/{0}?p={0}'.format(company[0]))
		soup = bs4.BeautifulSoup(url.text, features="html.parser")

		price = soup.find_all("div", {'class': 'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find('span').text
		price = price.replace(',','')
		price = float(price)

		cur.execute("UPDATE STOCKS SET CMP='{0}' WHERE COMPANY='{1}' ".format(price,company[0]))
		conn.commit()
	
	conn.close()
	return HttpResponse("Prices updated successfully!")


def updatepriceaction(request):			#this function updates open close high low in db
	conn = pymysql.connect( host='localhost',	port =3306 , user='root',  password = "123",   db='pgrdb' ) 
	cur = conn.cursor()
	cur.execute("SELECT company from STOCKS")
	conn.commit()
	companies = cur.fetchall()
	for company in companies:

		url = requests.get('https://finance.yahoo.com/quote/{0}?p={0}'.format(company[0]))
		soup = bs4.BeautifulSoup(url.text, features="html.parser")
		
		close = soup.find("td", {'data-test': 'PREV_CLOSE-value'}).text
		close = close.replace(',','')
		close = float(close)

		openp = soup.find("td", {'data-test': 'OPEN-value'}).text
		openp = openp.replace(',','')
		openp = float(openp)
		
		lowhigh = soup.find("td", {'data-test': 'DAYS_RANGE-value'}).text
		lowhigh = lowhigh.replace(',','')
		low,high = lowhigh.split(" - ")
		low = float(low)
		high = float(high)

		
		cur.execute("UPDATE STOCKS SET OPEN = '{0}', CLOSE = '{1}', HIGH = '{2}', LOW = '{3}' WHERE COMPANY='{4}' ".format(openp,close,high,low,company[0]))
		conn.commit()
	
	conn.close()
	return HttpResponse("Price Action updated successfully!")


def updateIndices(request):		#returns header indices data
	return HttpResponse(json.dumps(data.allIndices))

	# try:
	# 	import json
	# 	url = requests.get('https://www.moneycontrol.com/markets/irol.com/markets/indian-indices/?classic=true', timeout=5)
	# 	soup = bs4.BeautifulSoup(url.text, features="html.parser")
	# 	indices = {
	#         "NIFTY50":soup.find_all("td", {'align': 'right'})[6].text ,
	#         "NIFTY50CHNG":soup.find_all("td", {'align': 'right'})[7].text,
	#         "NIFTY50PCHNG":soup.find_all("td", {'align': 'right'})[8].text,
	#         "NIFTYBANK":soup.find_all("td", {'align': 'right'})[276].text,
	#         "NIFTYBANKCHNG":soup.find_all("td", {'align': 'right'})[277].text,
	#         "NIFTYBANKPCHNG":soup.find_all("td", {'align': 'right'})[278].text,
	#         "NIFTYENERGY":soup.find_all("td", {'align': 'right'})[294].text,
	#         "NIFTYENERGYCHNG":soup.find_all("td", {'align': 'right'})[295].text,
	#         "NIFTYENERGYPCHNG":soup.find_all("td", {'align': 'right'})[296].text,
	#         "NIFTYIT":soup.find_all("td", {'align': 'right'})[318].text,
	#         "NIFTYITCHNG":soup.find_all("td", {'align': 'right'})[319].text,
	#         "NIFTYITPCHNG":soup.find_all("td", {'align': 'right'})[320].text
	#         }
	# 	return HttpResponse(json.dumps(indices))
	# except Exception as e:
	# 	import json
	# 	url = requests.get('https://www.moneycontrol.com/markets/irol.com/markets/indian-indices/?classic=true', timeout=5)
	# 	soup = bs4.BeautifulSoup(url.text, features="html.parser")
	# 	indices = {
	#         "NIFTY50":soup.find_all("td", {'align': 'right'})[6].text ,
	#         "NIFTY50CHNG":soup.find_all("td", {'align': 'right'})[7].text,
	#         "NIFTY50PCHNG":soup.find_all("td", {'align': 'right'})[8].text,
	#         "NIFTYBANK":soup.find_all("td", {'align': 'right'})[276].text,
	#         "NIFTYBANKCHNG":soup.find_all("td", {'align': 'right'})[277].text,
	#         "NIFTYBANKPCHNG":soup.find_all("td", {'align': 'right'})[278].text,
	#         "NIFTYENERGY":soup.find_all("td", {'align': 'right'})[294].text,
	#         "NIFTYENERGYCHNG":soup.find_all("td", {'align': 'right'})[295].text,
	#         "NIFTYENERGYPCHNG":soup.find_all("td", {'align': 'right'})[296].text,
	#         "NIFTYIT":soup.find_all("td", {'align': 'right'})[318].text,
	#         "NIFTYITCHNG":soup.find_all("td", {'align': 'right'})[319].text,
	#         "NIFTYITPCHNG":soup.find_all("td", {'align': 'right'})[320].text
	#         }
	# 	return HttpResponse(json.dumps(indices))
	# except:
	# 	return HttpResponse(json.dumps("True"))



def updateAllIndices(request):		#returns indices data
	return HttpResponse(json.dumps(data.allIndices))
	# try:
	# 	import json
	# 	url = requests.get('https://www.moneycontrol.com/markets/irol.com/markets/indian-indices/?classic=true', timeout=5)
	# 	soup = bs4.BeautifulSoup(url.text, features="html.parser")
	# 	i = 0
	# 	pricel=[]
	# 	chngl=[]
	# 	pchngl=[]
	# 	for i in range(70):
	# 		if (i==1 or ((i>39) and (i<63))):
	# 			price = soup.find_all("td", {'align': 'right'})[6*i].text
	# 			price=price.replace(',','')
	# 			price = float(price)
	# 			chng = soup.find_all("td", {'align': 'right'})[6*i+1].text
	# 			pchng = soup.find_all("td", {'align': 'right'})[6*i+2].text
	# 			pricel.append(price)
	# 			chngl.append(chng)
	# 			pchngl.append(pchng)
	# 	data = {"price":pricel, "chng": chngl, "pchng":pchngl} 
	# 	return HttpResponse(json.dumps(data))
	# except:
	# 	return HttpResponse(json.dumps("True"))



def update_index_page(request):
	try:
		value = [9,27,31,53,28,7,52,23,48,56,38,47,39,35,19,50,51,40,41,42,43,79,34,44]
		indices = ['NIFTY 50', 'NIFTY Midcap 100', 'NIFTY MIDCAP 50', 'NIFTY Smallcap 100', 'NIFTY 100', 'NIFTY 500', 'NIFTY AUTO', 'NIFTY BANK', 'NIFTY COMMODITIES', 'NIFTY CONSUMPTION', 'NIFTY ENERGY', 'NIFTY FIN SERVICE', 'NIFTY FMCG', 'NIFTY INFRA', 'NIFTY IT', 'NIFTY MEDIA', 'NIFTY METAL', 'NIFTY MNC', 'NIFTY PHARMA', 'NIFTY PSE', 'NIFTY PSU BANK', 'NIFTY PVT BANK', 'NIFTY REALTY', 'NIFTY SERV SECTOR']
		ticker = str(request.GET.get('ticker', None))
		index_value = value[indices.index(ticker)]
		url = requests.get('https://www.moneycontrol.com/stocks/marketstats/indexcomp.php?optex=NSE&opttopic=indexcomp&index={0}'.format(index_value))
		soup = bs4.BeautifulSoup(url.text, features="html.parser")
		i = 0
		tickerl = []
		pricel=[]
		chngl=[]
		pchngl=[]
		res = soup.find_all("td", {"class":"brdrgtgry"})
		try:
		    while(True):
		        tickerl.append(res[i].text.split("\n")[0])
		        pricel.append(res[i+2].text.replace(',',''))
		        chngl.append(res[i+3].text)
		        pchngl.append(res[i+4].text)
		        i+=6
		except:
		    True
		data = {"ticker":tickerl, "price":pricel, "chng": chngl, "pchng":pchngl} 
		return HttpResponse(json.dumps(data))

	except:
		return HttpResponse(json.dumps("True"))
