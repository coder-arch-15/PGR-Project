from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
import pymysql
import json
import bs4
import requests
from bs4 import BeautifulSoup
import pymysql as mysql
from . import hreflist as hf

def update1shownifty500(request):
    url = requests.get('https://www.moneycontrol.com/stocks/marketstats/indexcomp.php?optex=NSE&opttopic=indexcomp&index=7')
    soup = bs4.BeautifulSoup(url.text, features="html.parser")
    res = soup.find_all("td", {'align': 'right'})
    i = 0
    pricel=[]
    chngl=[]
    pchngl=[]

    
    while(i>=0 and i<200):
        price = res[i].text
        price=price.replace(',','')
        chng = res[i + 1].text
        pchng = res[i + 2].text
        pricel.append(price)
        chngl.append(chng)
        pchngl.append(pchng)
        i += 4
    data = {"price": pricel, "chng": chngl, "pchng": pchngl}
    return HttpResponse(json.dumps(data))

def update2shownifty500(request):
    url = requests.get('https://www.moneycontrol.com/stocks/marketstats/indexcomp.php?optex=NSE&opttopic=indexcomp&index=7')
    soup = bs4.BeautifulSoup(url.text, features="html.parser")
    res = soup.find_all("td", {'align': 'right'})
    i = 200
    pricel=[]
    chngl=[]
    pchngl=[]
    
    while(i>=200 and i<400):
        price = res[i].text
        price=price.replace(',','')
        chng = res[i + 1].text
        pchng = res[i + 2].text
        pricel.append(price)
        chngl.append(chng)
        pchngl.append(pchng)
        i += 4
    data = {"price": pricel, "chng": chngl, "pchng": pchngl}
    return HttpResponse(json.dumps(data))

def update3shownifty500(request):
    url = requests.get('https://www.moneycontrol.com/stocks/marketstats/indexcomp.php?optex=NSE&opttopic=indexcomp&index=7')
    soup = bs4.BeautifulSoup(url.text, features="html.parser")
    res = soup.find_all("td", {'align': 'right'})
    i = 400
    pricel=[]
    chngl=[]
    pchngl=[]
    
    while(i>=400 and i<600):
        price = res[i].text
        price=price.replace(',','')
        chng = res[i + 1].text
        pchng = res[i + 2].text
        pricel.append(price)
        chngl.append(chng)
        pchngl.append(pchng)
        i += 4
    data = {"price": pricel, "chng": chngl, "pchng": pchngl}
    return HttpResponse(json.dumps(data))

def update4shownifty500(request):
    url = requests.get('https://www.moneycontrol.com/stocks/marketstats/indexcomp.php?optex=NSE&opttopic=indexcomp&index=7')
    soup = bs4.BeautifulSoup(url.text, features="html.parser")
    res = soup.find_all("td", {'align': 'right'})
    i = 600
    pricel=[]
    chngl=[]
    pchngl=[]

    
    while(i>=600 and i<800):
        price = res[i].text
        price=price.replace(',','')
        chng = res[i + 1].text
        pchng = res[i + 2].text
        pricel.append(price)
        chngl.append(chng)
        pchngl.append(pchng)
        i += 4
    data = {"price": pricel, "chng": chngl, "pchng": pchngl}
    return HttpResponse(json.dumps(data))

def update5shownifty500(request):
    url = requests.get('https://www.moneycontrol.com/stocks/marketstats/indexcomp.php?optex=NSE&opttopic=indexcomp&index=7')
    soup = bs4.BeautifulSoup(url.text, features="html.parser")
    res = soup.find_all("td", {'align': 'right'})
    i = 800
    pricel=[]
    chngl=[]
    pchngl=[]

    
    while(i>=800 and i<1000):
        price = res[i].text
        price=price.replace(',','')
        chng = res[i + 1].text
        pchng = res[i + 2].text
        pricel.append(price)
        chngl.append(chng)
        pchngl.append(pchng)
        i += 4
    data = {"price": pricel, "chng": chngl, "pchng": pchngl}
    return HttpResponse(json.dumps(data))

def update6shownifty500(request):
    url = requests.get('https://www.moneycontrol.com/stocks/marketstats/indexcomp.php?optex=NSE&opttopic=indexcomp&index=7')
    soup = bs4.BeautifulSoup(url.text, features="html.parser")
    res = soup.find_all("td", {'align': 'right'})
    i = 1000
    pricel=[]
    chngl=[]
    pchngl=[]

    y = ['3M India','Aarti Ind','AAVAS Financier','AB Capital','ABB India','Abbott India','ACC','Adani Ports','Adani Power','Adani Total Gas','Adani Trans','Aditya Birla F','Advanced Enzyme','Aegis Logistics','AFL','AIA Engineering','Ajanta Pharma','Akzo Nobel','Alembic Pharma','Alkem Lab','Alkyl Amines','Allcargo','Amara Raja Batt','Amber Enterpris','Ambuja Cements','APL Apollo','Apollo Hospital','Apollo Tyres','Asahi India','Ashok Leyland','Ashoka Buildcon','Asian Paints','Aster DM Health','Astral Poly Tec','AstraZeneca','Atul','AU Small Financ','Aurobindo Pharm','Avanti Feeds','Avenue Supermar','Axis Bank','Bajaj Auto','Bajaj Consumer','Bajaj Electric','Bajaj Finance','Bajaj Finserv','Bajaj Holdings','Balkrishna Ind','Balmer Lawrie','Balrampur Chini','Bandhan Bank','Bank of Baroda','Bank of India','Bank of Mah','BASF','Bata India','Bayer CropScien','BEML','Berger Paints','Bharat Dynamics','Bharat Elec','Bharat Forge','Bharat Rasayan','Bharti Airtel','BHEL','Biocon','Birla Corp','Birlasoft','Bliss GVS','Blue Dart','Blue Star','Bombay Burmah','Bombay Dyeing','Bosch','BPCL','Brigade Ent','Britannia','BSE Limited','Cadila Health','Can Fin Homes','Canara Bank','Caplin Labs','Capri Global','Carborundum','CARE Ratings','Castrol','CCL Products','CDSL','Ceat','Central Bank','Century','CenturyPlyboard','Cera Sanitary','CESC Power','CG Consumer','Chambal Fert','Chennai Petro','Cholamandalam','Cholamandalam','Cipla','City Union Bank','Coal India','Cochin Shipyard','COFORGE LTD.','Colgate','Container Corp','Coromandel Int','CreditAccess Gr','CRISIL','Cummins','Cyient','Dabur India','Dalmia Bharat','DB Corp','DCB Bank','DCM Shriram','Deepak Nitrite','Delta Corp','Dhani Services','Dhanuka Agritec','Dilip Buildcon','Dish TV','Dishman Carboge','Divis Labs','Dixon Technolog','DLF','Dr Lal PathLab','Dr Reddys Labs','eClerx Services','Edelweiss','Eicher Motors','EID Parry','EIH,Elgi Equipments','Emami','Endurance Techn']

    while(i>=1000 and i<1200):
        price = res[i].text
        price=price.replace(',','')
        chng = res[i + 1].text
        pchng = res[i + 2].text
        pricel.append(price)
        chngl.append(chng)
        pchngl.append(pchng)
        i += 4
    data = {"price": pricel, "chng": chngl, "pchng": pchngl}
    return HttpResponse(json.dumps(data))

def update7shownifty500(request):
    url = requests.get('https://www.moneycontrol.com/stocks/marketstats/indexcomp.php?optex=NSE&opttopic=indexcomp&index=7')
    soup = bs4.BeautifulSoup(url.text, features="html.parser")
    res = soup.find_all("td", {'align': 'right'})
    i = 1200
    pricel=[]
    chngl=[]
    pchngl=[]

    y = ['3M India','Aarti Ind','AAVAS Financier','AB Capital','ABB India','Abbott India','ACC','Adani Ports','Adani Power','Adani Total Gas','Adani Trans','Aditya Birla F','Advanced Enzyme','Aegis Logistics','AFL','AIA Engineering','Ajanta Pharma','Akzo Nobel','Alembic Pharma','Alkem Lab','Alkyl Amines','Allcargo','Amara Raja Batt','Amber Enterpris','Ambuja Cements','APL Apollo','Apollo Hospital','Apollo Tyres','Asahi India','Ashok Leyland','Ashoka Buildcon','Asian Paints','Aster DM Health','Astral Poly Tec','AstraZeneca','Atul','AU Small Financ','Aurobindo Pharm','Avanti Feeds','Avenue Supermar','Axis Bank','Bajaj Auto','Bajaj Consumer','Bajaj Electric','Bajaj Finance','Bajaj Finserv','Bajaj Holdings','Balkrishna Ind','Balmer Lawrie','Balrampur Chini','Bandhan Bank','Bank of Baroda','Bank of India','Bank of Mah','BASF','Bata India','Bayer CropScien','BEML','Berger Paints','Bharat Dynamics','Bharat Elec','Bharat Forge','Bharat Rasayan','Bharti Airtel','BHEL','Biocon','Birla Corp','Birlasoft','Bliss GVS','Blue Dart','Blue Star','Bombay Burmah','Bombay Dyeing','Bosch','BPCL','Brigade Ent','Britannia','BSE Limited','Cadila Health','Can Fin Homes','Canara Bank','Caplin Labs','Capri Global','Carborundum','CARE Ratings','Castrol','CCL Products','CDSL','Ceat','Central Bank','Century','CenturyPlyboard','Cera Sanitary','CESC Power','CG Consumer','Chambal Fert','Chennai Petro','Cholamandalam','Cholamandalam','Cipla','City Union Bank','Coal India','Cochin Shipyard','COFORGE LTD.','Colgate','Container Corp','Coromandel Int','CreditAccess Gr','CRISIL','Cummins','Cyient','Dabur India','Dalmia Bharat','DB Corp','DCB Bank','DCM Shriram','Deepak Nitrite','Delta Corp','Dhani Services','Dhanuka Agritec','Dilip Buildcon','Dish TV','Dishman Carboge','Divis Labs','Dixon Technolog','DLF','Dr Lal PathLab','Dr Reddys Labs','eClerx Services','Edelweiss','Eicher Motors','EID Parry','EIH,Elgi Equipments','Emami','Endurance Techn']

    while(i>=1200 and i<1400):
        price = res[i].text
        price=price.replace(',','')
        chng = res[i + 1].text
        pchng = res[i + 2].text
        pricel.append(price)
        chngl.append(chng)
        pchngl.append(pchng)
        i += 4
    data = {"price": pricel, "chng": chngl, "pchng": pchngl}
    return HttpResponse(json.dumps(data))

def update8shownifty500(request):
    url = requests.get('https://www.moneycontrol.com/stocks/marketstats/indexcomp.php?optex=NSE&opttopic=indexcomp&index=7')
    soup = bs4.BeautifulSoup(url.text, features="html.parser")
    res = soup.find_all("td", {'align': 'right'})
    i = 1400
    pricel=[]
    chngl=[]
    pchngl=[]
    while(i>=1400 and i<1600):
        price = res[i].text
        price=price.replace(',','')
        chng = res[i + 1].text
        pchng = res[i + 2].text
        pricel.append(price)
        chngl.append(chng)
        pchngl.append(pchng)
        i += 4
    data = {"price": pricel, "chng": chngl, "pchng": pchngl}
    return HttpResponse(json.dumps(data))

def update9shownifty500(request):
    url = requests.get('https://www.moneycontrol.com/stocks/marketstats/indexcomp.php?optex=NSE&opttopic=indexcomp&index=7')
    soup = bs4.BeautifulSoup(url.text, features="html.parser")
    res = soup.find_all("td", {'align': 'right'})
    i = 1600
    pricel=[]
    chngl=[]
    pchngl=[]


    while(i>=1600 and i<1800):
        price = res[i].text
        price=price.replace(',','')
        chng = res[i + 1].text
        pchng = res[i + 2].text
        pricel.append(price)
        chngl.append(chng)
        pchngl.append(pchng)
        i += 4
    data = {"price": pricel, "chng": chngl, "pchng": pchngl}
    return HttpResponse(json.dumps(data))

def update10shownifty500(request):
    url = requests.get('https://www.moneycontrol.com/stocks/marketstats/indexcomp.php?optex=NSE&opttopic=indexcomp&index=7')
    soup = bs4.BeautifulSoup(url.text, features="html.parser")
    res = soup.find_all("td", {'align': 'right'})
    i = 1800
    pricel=[]
    chngl=[]
    pchngl=[]

    while(i>=1800 and i<1956):
        price = res[i].text
        price=price.replace(',','')
        chng = res[i + 1].text
        pchng = res[i + 2].text
        pricel.append(price)
        chngl.append(chng)
        pchngl.append(pchng)
        i += 4
    data = {"price": pricel, "chng": chngl, "pchng": pchngl}
    return HttpResponse(json.dumps(data))


def shownifty500(request):
    rec = []
    for key in hf.codes.keys():
        rec.append(key)
    return render(request,"nifty500.html",{'stocks': rec})

# def temp(request):
#     url = requests.get('https://www.moneycontrol.com/stocks/marketstats/indexcomp.php?optex=NSE&opttopic=indexcomp&index=7')
#     soup = bs4.BeautifulSoup(url.text, features="html.parser")
#     i=0
#     com=[]
#     while(i<489):
#         company = soup.find_all("td", {'width': '24%'})[i].text
#         a=company.index("\n")
#         com.append(company[0:a])
#         i+=1
#
#     dbe = mysql.connect(host='localhost', port=3306, password='123', user='root', db='pgrdb')
#     cmd = dbe.cursor()
#     for i in range(99,489):
#         q="insert into stocks500 values('{0}')".format(com[i])
#         cmd.execute(q)
#     dbe.commit()
#     dbe.close()
#     return render(request,"nifty500.html")

