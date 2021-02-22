from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
import pymysql
import json
import bs4
import requests
from bs4 import BeautifulSoup

def shownifty500(request):
    url = requests.get(
        'https://www.moneycontrol.com/stocks/marketstats/indexcomp.php?optex=NSE&opttopic=indexcomp&index=7')
    soup = bs4.BeautifulSoup(url.text, features="html.parser")
    tickers = []
    i = 0
    pricel=[]
    chngl=[]
    pchngl=[]
    y = ['ADANIPORTS.NS', 'ASIANPAINT.NS', 'AXISBANK.NS', 'BAJAJ-AUTO.NS', 'BAJAJFINSV.NS', 'BAJFINANCE.NS', 'BHARTIARTL.NS', 'BPCL.NS', 'BRITANNIA.NS', 'CIPLA.NS', 'COALINDIA.NS', 'DIVISLAB.NS', 'DRREDDY.NS', 'EICHERMOT.NS', 'GAIL.NS', 'GRASIM.NS', 'HCLTECH.NS', 'HDFC.NS', 'HDFCBANK.NS', 'HDFCLIFE.NS', 'HEROMOTOCO.NS', 'HINDALCO.NS', 'HINDUNILVR.NS', 'ICICIBANK.NS', 'INDUSINDBK.NS', 'INFY.NS', 'IOC.NS', 'ITC.NS', 'JSWSTEEL.NS', 'KOTAKBANK.NS', 'LT.NS', 'M&M.NS', 'MARUTI.NS', 'NESTLEIND.NS', 'NTPC.NS', 'ONGC.NS', 'POWERGRID.NS', 'RELIANCE.NS', 'SBILIFE.NS', 'SBIN.NS', 'SHREECEM.NS', 'SUNPHARMA.NS', 'TATAMOTORS.NS', 'TATASTEEL.NS', 'TCS.NS', 'TECHM.NS', 'TITAN.NS', 'ULTRACEMCO.NS', 'UPL.NS', 'WIPRO.NS']
    while (i < 200):
    	price = soup.find_all("td", {'align': 'right'})[i].text
    	price=price.replace(',','')
    	chng = soup.find_all("td", {'align': 'right'})[i + 1].text
    	pchng = soup.find_all("td", {'align': 'right'})[i + 2].text
    	pricel.append(price)
    	chngl.append(chng)
    	pchngl.append(pchng)
    	i += 4
    while (i >= 200 and i<400):
    	price = soup.find_all("td", {'align': 'right'})[i].text
    	price=price.replace(',','')
    	chng = soup.find_all("td", {'align': 'right'})[i + 1].text
    	pchng = soup.find_all("td", {'align': 'right'})[i + 2].text
    	pricel.append(price)
    	chngl.append(chng)
    	pchngl.append(pchng)
    	i += 4
    data = {"price":pricel, "chng": chngl, "pchng":pchngl}
    return HttpResponse(json.dumps(data))