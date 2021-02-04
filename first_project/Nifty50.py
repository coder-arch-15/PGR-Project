from django.shortcuts import render
import pymysql as mysql
import bs4
import requests
from bs4 import BeautifulSoup
from difflib import get_close_matches


def ActionShowNifty50(request):
    url = requests.get(
        'https://www.moneycontrol.com/stocks/marketstats/indexcomp.php?optex=NSE&opttopic=indexcomp&index=9')
    soup = bs4.BeautifulSoup(url.text, features="html.parser")
    tickers = []
    i = 0
    pricel=[]
    chngl=[]
    pchngl=[]

    while (i < 200):
        price = soup.find_all("td", {'align': 'right'})[i].text
        chng = soup.find_all("td", {'align': 'right'})[i + 1].text
        pchng = soup.find_all("td", {'align': 'right'})[i + 2].text
        pricel.append(price)
        chngl.append(chng)
        pchngl.append(pchng)
        i += 4
    dbe = mysql.connect(host='localhost', port=3306, password='123', user='root', db='pgrdb')
    cmd = dbe.cursor()
    q = "select * from stocks"
    cmd.execute(q)
    rec = cmd.fetchall()
    return render(request,"nifty50page.html",{'stocks':rec,'price':pricel,'chng':chngl,'pchng':pchngl})

def ActionBuySellForm(request):
    return render(request, "buysellform.html")
