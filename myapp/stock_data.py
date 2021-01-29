from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings 
import pymysql

import bs4
import requests
from bs4 import BeautifulSoup 

def getcmp(request,ticker):
	#ticker = request.GET.get("ticker")
	url = requests.get("https://finance.yahoo.com/quote/{0}?p={0}".format(ticker))
	soup = bs4.BeautifulSoup(url.text, features="html.parser")
	price = soup.find_all("div", {'class': 'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find('span').text
	price=float(price.replace(',',''))
	return HttpResponse(price)


def updatecmp(request):
	conn = pymysql.connect( 
			        host='localhost',
					port =3306 ,
			        user='root',  

			        password = "123",

			        db='pgrdb', 
			        ) 
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
		cur.execute("UPDATE STOCKS SET CMP='{0}', OPEN = '{1}', CLOSE = '{2}', HIGH = '{3}', LOW = '{4}' WHERE COMPANY='{5}' ".format(price,openp,close,high,low,company[0]))
		conn.commit()
	conn.commit()
	conn.close()