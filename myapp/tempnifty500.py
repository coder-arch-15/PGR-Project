from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect, StreamingHttpResponse
from django.conf import settings
import pymysql
import json
import bs4
import requests
from bs4 import BeautifulSoup
import pymysql as mysql
from . import hreflist as hf
from . import data 

def generator_updateshownifty500(soup):
    
    # tickers = []
    i = -1
    # pricel=[]
    # chngl=[]
    # pchngl=[]
    try:
        while(True):
            # ticker = soup.find_all("td", {"class":"brdrgtgry"})[i].text.split("\n")[0]
            # industry = soup.find_all("td", {"class":"brdrgtgry"})[i+1].text
            # price = soup.find_all("td", {"class":"brdrgtgry"})[i+2].text
            # price = price.replace(',','')
            # chng = soup.find_all("td", {"class":"brdrgtgry"})[i+3].text
            # pchng = soup.find_all("td", {"class":"brdrgtgry"})[i+4].text
            # i += 6
            # data = {"ticker":ticker, "price":price, "chng": chng, "pchng":pchng}
            i+=1
            yield json.dumps(data.nifty500data[i])
    except:
        True


def tempupdateshownifty500(request):
    return HttpResponse(json.dumps(data.nifty500data))


def tempshownifty500(request):
    
    rec = []
    for key in hf.codes.keys():
        rec.append(key)
    return render(request,"temp2nifty500.html",{'stocks': rec})

