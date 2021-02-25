from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail
from django.conf import settings 
import pymysql
import bs4
import requests
from bs4 import BeautifulSoup  
from . import hreflist

def user_dashboard(request):
	if(request.session.has_key("user")):
		if( int(request.session['user'][5]) != 0):
			return render(request, "userdashboard.html")
		else:
			return redirect("/buyplanpage")
	else:
		return redirect("/login")


def buyplanpage(request):
	if(request.session.has_key("user")):
		error = request.GET.get('error', None)
		if error is not None:
			return render(request, "buymembershipp.html", {"error":error})
		else:
			return render(request, "buymembershipp.html")
	else:
		return redirect("/login")
	



def stockpage(request):
	if(request.session.has_key("user")):
		if( int(request.session['user'][5]) != 0):
			ticker = str(request.GET.get('ticker', None))
			tradingview_ticker=ticker.split(".NS")

			conn = pymysql.connect( host='localhost',	port =3306 , user='root',  password = "123",   db='pgrdb' ) 
			cur = conn.cursor()
			
			cur.execute("SELECT * FROM STOCKS WHERE company = '{0}'".format(ticker))
			stocks = cur.fetchone()
			cur.execute("SELECT quantity FROM HOLDINGS WHERE company = '{0}' and username = '{0}'".format(ticker, request.session['user'][0]))
			if cur.rowcount==0:
				current_holdings =[0]
			else:
				current_holdings = cur.fetchone()
			conn.commit()
			conn.close()
			return render(request, "stockpage.html", {"info":stocks,"tradingview_ticker":tradingview_ticker[0], "cash":request.session['user'][9], "current_holdings": current_holdings[0] })
		else:
			return redirect("/buyplanpage")
	else:
		return redirect("/login")


def advanceStockChart(request):
	ticker = str(request.GET.get('ticker', None))
	tradingview_ticker=ticker.split(".NS")
	return render(request, "advstockchart.html", {"tradingview_ticker":tradingview_ticker[0]})


def user_show_stocks(request):
	if(request.session.has_key("user")):
		if( int(request.session['user'][5]) >= 1):
			return render(request, "usershowstocks.html")
		else:
			return redirect("/buyplanpage/?error=To access NIFTY-50 STOCKS section please activate SILVER or any premium plan!")
	else:
		return redirect("/login")


def user_adv_stocks(request):
	if(request.session.has_key("user")):
		if( int(request.session['user'][5]) >= 2):
			return render(request, "useradvstocks.html")
		else:
			return redirect("/buyplanpage/?error=To access ADVANCE STOCKS section please activate GOLD or any premium plan!")
	else:
		return redirect("/login")


def user_analysis(request):
	if(request.session.has_key("user")):
		if( int(request.session['user'][5]) >= 3):
			print("hello_analysis")
			return render(request, "useranalysis.html")
		else:
			return redirect("/buyplanpage/?error=To access STOCKS ANALYSIS section please activate DIAMOND or any premium plan!")
	else:
		return redirect("/login")


def user_watchlist(request):
	if(request.session.has_key("user")):
		if( int(request.session['user'][5]) >= 1):
			print("hello_watchlist")
			return render(request, "userwatchlist.html")
		else:
			return redirect("/buyplanpage/?error=To access WATCHLIST section please activate SILVER or any premium plan!")
	else:
		return redirect("/login")


def user_wallet(request):
	if(request.session.has_key("user")):
		if( int(request.session['user'][5]) >= 1):
			conn = pymysql.connect( host='localhost',	port =3306 , user='root',  password = "123",   db='pgrdb' ) 
			cur = conn.cursor()
			cur.execute("SELECT * FROM STOCKS")
			stocks = cur.fetchall()
			cur.execute("SELECT * FROM HOLDINGS WHERE username = '{0}'".format(request.session['user'][0]))
			table = cur.fetchall()
			cur.execute("SELECT company FROM HOLDINGS WHERE username = '{0}'".format(request.session['user'][0]))
			stocklist = cur.fetchall()
			conn.commit()
			conn.close()
			
			return render(request, "userwallet.html", {"table": table , "stocks": stocks, "stocklist":stocklist})
		else:
			return redirect("/buyplanpage/?error=To access WALLET section please activate SILVER or any premium plan!")
	else:
		return redirect("/login")


def user_transaction(request):
	if(request.session.has_key("user")):
		if( int(request.session['user'][5]) >= 1):
			print("hello_transaction")
			return render(request, "usertransaction.html")
		else:
			return redirect("/buyplanpage/?error=To access TRANSACTIONS section please activate SILVER or any premium plan!")
	else:
		return redirect("/login")


def user_membership_account(request):
	if(request.session.has_key("user")):
		print("hello_account")
		return render(request, "useraccount.html")
	else:
		return redirect("/login")



def user_leaderboard(request):
	if(request.session.has_key("user")):
		if( int(request.session['user'][5]) >= 1):
			print("hello_leaderboard")
			return render(request, "userleaderboard.html")
		else:
			return redirect("/buyplanpage/?error=To access LEADERBOARD section please activate SILVER or any premium plan!")
	else:
		return redirect("/login")


def user_buyplan(request,planid,expiry):
	if(request.session.has_key("user")):
		from datetime import datetime, timedelta
		planid = int(planid)

		if(expiry=="1"):
			expirydate = datetime.now() + timedelta(days=30) 
		elif(expiry=="2"):
			expirydate = datetime.now() + timedelta(days=90) 
		elif(expiry=="3"):
			expirydate = datetime.now() + timedelta(days=182) 
		elif(expiry=="4"):
			expirydate = datetime.now() + timedelta(days=365) 
		else:
			expirydate = ""
		conn = pymysql.connect( host='localhost',	port =3306 , user='root',  password = "123",   db='pgrdb' ) 
		cur = conn.cursor()
		q="UPDATE USERS SET plan = '{0}', pending = '{1}', approved = '{2}', expiry = '{3}' WHERE username='{4}'".format(planid,1,0,expirydate,request.session['user'][0])
		cur.execute(q)
		cur.execute("SELECT * FROM users WHERE username='{0}'".format(request.session['user'][0]))
		user= cur.fetchone()
		request.session['user'] = user
		conn.commit()
		conn.close()		
		return redirect("/userdashboard")
	else:
		return redirect("/login")


def user_logout(request):
	try:
		del request.session['user']
	except:
		pass
	return redirect('/')



def all_indices(request):
	if(request.session.has_key("user")):
		indices = ['NIFTY 50', 'NIFTY Midcap 100', 'NIFTY MIDCAP 50', 'NIFTY Smallcap 100', 'NIFTY 100', 'NIFTY 500', 'NIFTY AUTO', 'NIFTY BANK', 'NIFTY COMMODITIES', 'NIFTY CONSUMPTION', 'NIFTY ENERGY', 'NIFTY FIN SERVICE', 'NIFTY FMCG', 'NIFTY INFRA', 'NIFTY IT', 'NIFTY MEDIA', 'NIFTY METAL', 'NIFTY MNC', 'NIFTY PHARMA', 'NIFTY PSE', 'NIFTY PSU BANK', 'NIFTY PVT BANK', 'NIFTY REALTY', 'NIFTY SERV SECTOR']
		return render(request, "indices.html", {"indices":indices})
	else:
		return redirect("/login")


def index_page(request):
	if(request.session.has_key("user")):
		value = [9,27,31,53,28,7,52,23,48,56,38,47,39,35,19,50,51,40,41,42,43,79,34,44]
		indices = ['NIFTY 50', 'NIFTY Midcap 100', 'NIFTY MIDCAP 50', 'NIFTY Smallcap 100', 'NIFTY 100', 'NIFTY 500', 'NIFTY AUTO', 'NIFTY BANK', 'NIFTY COMMODITIES', 'NIFTY CONSUMPTION', 'NIFTY ENERGY', 'NIFTY FIN SERVICE', 'NIFTY FMCG', 'NIFTY INFRA', 'NIFTY IT', 'NIFTY MEDIA', 'NIFTY METAL', 'NIFTY MNC', 'NIFTY PHARMA', 'NIFTY PSE', 'NIFTY PSU BANK', 'NIFTY PVT BANK', 'NIFTY REALTY', 'NIFTY SERV SECTOR']
		tick = str(request.GET.get('ticker', None))
		index_value = value[indices.index(tick)]
		url = requests.get('https://www.moneycontrol.com/stocks/marketstats/indexcomp.php?optex=NSE&opttopic=indexcomp&index={0}'.format(index_value))
		soup = bs4.BeautifulSoup(url.text, features="html.parser")
		i = 0
		tickerl = []
		pricel=[]
		industryl  =[]
		chngl=[]
		pchngl=[]
		try:
		    while(True):
		        ticker = soup.find_all("td", {"class":"brdrgtgry"})[i].text.split("\n")[0]
		        industry = soup.find_all("td", {"class":"brdrgtgry"})[i+1].text
		        price = soup.find_all("td", {"class":"brdrgtgry"})[i+2].text
		        chng = soup.find_all("td", {"class":"brdrgtgry"})[i+3].text
		        pchng = soup.find_all("td", {"class":"brdrgtgry"})[i+4].text
		        i+=6
		        industryl.append(industry)
		        tickerl.append(ticker)
		        pricel.append(price)
		        chngl.append(chng)
		        pchngl.append(pchng)
		except:
		    True
		data = {"ticker":tickerl, "industry":industryl, "price":pricel, "chng": chngl, "pchng":pchngl} 
		return render(request, "indexpage.html", {"stocks": tickerl, "index":tick})
	else:
		return redirect("/login")