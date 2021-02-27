from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
import pymysql
import json
import bs4
import requests
from bs4 import BeautifulSoup
import pymysql as mysql

def updateshownifty500(request):
    url = requests.get('https://www.moneycontrol.com/stocks/marketstats/indexcomp.php?optex=NSE&opttopic=indexcomp&index=7')
    soup = bs4.BeautifulSoup(url.text, features="html.parser")
    tickers = []
    i = 0
    pricel=[]
    chngl=[]
    pchngl=[]
    min=0
    max=200
    y = ['3M India','Aarti Ind','AAVAS Financier','AB Capital','ABB India','Abbott India','ACC','Adani Ports','Adani Power','Adani Total Gas','Adani Trans','Aditya Birla F','Advanced Enzyme','Aegis Logistics','AFL','AIA Engineering','Ajanta Pharma','Akzo Nobel','Alembic Pharma','Alkem Lab','Alkyl Amines','Allcargo','Amara Raja Batt','Amber Enterpris','Ambuja Cements','APL Apollo','Apollo Hospital','Apollo Tyres','Asahi India','Ashok Leyland','Ashoka Buildcon','Asian Paints','Aster DM Health','Astral Poly Tec','AstraZeneca','Atul','AU Small Financ','Aurobindo Pharm','Avanti Feeds','Avenue Supermar','Axis Bank','Bajaj Auto','Bajaj Consumer','Bajaj Electric','Bajaj Finance','Bajaj Finserv','Bajaj Holdings','Balkrishna Ind','Balmer Lawrie','Balrampur Chini','Bandhan Bank','Bank of Baroda','Bank of India','Bank of Mah','BASF','Bata India','Bayer CropScien','BEML','Berger Paints','Bharat Dynamics','Bharat Elec','Bharat Forge','Bharat Rasayan','Bharti Airtel','BHEL','Biocon','Birla Corp','Birlasoft','Bliss GVS','Blue Dart','Blue Star','Bombay Burmah','Bombay Dyeing','Bosch','BPCL','Brigade Ent','Britannia','BSE Limited','Cadila Health','Can Fin Homes','Canara Bank','Caplin Labs','Capri Global','Carborundum','CARE Ratings','Castrol','CCL Products','CDSL','Ceat','Central Bank','Century','CenturyPlyboard','Cera Sanitary','CESC Power','CG Consumer','Chambal Fert','Chennai Petro','Cholamandalam','Cholamandalam','Cipla','City Union Bank','Coal India','Cochin Shipyard','COFORGE LTD.','Colgate','Container Corp','Coromandel Int','CreditAccess Gr','CRISIL','Cummins','Cyient','Dabur India','Dalmia Bharat','DB Corp','DCB Bank','DCM Shriram','Deepak Nitrite','Delta Corp','Dhani Services','Dhanuka Agritec','Dilip Buildcon','Dish TV','Dishman Carboge','Divis Labs','Dixon Technolog','DLF','Dr Lal PathLab','Dr Reddys Labs','eClerx Services','Edelweiss','Eicher Motors','EID Parry','EIH,Elgi Equipments','Emami','Endurance Techn']
    while(max<2000):
      while(i>=min and i<max):
        price = soup.find_all("td", {'align': 'right'})[i].text
        price=price.replace(',','')
        chng = soup.find_all("td", {'align': 'right'})[i + 1].text
        pchng = soup.find_all("td", {'align': 'right'})[i + 2].text
        pricel.append(price)
        chngl.append(chng)
        pchngl.append(pchng)
        i += 4
    data = {"price": pricel, "chng": chngl, "pchng": pchngl}
    return HttpResponse(json.dumps(data))
    # while(i>=200 and i<400):
    #     price = soup.find_all("td", {'align':'right'})[i].text
    #     price = price.replace(',','')
    #     chng = soup.find_all("td", {'align':'right'})[i + 1].text
    #     pchng = soup.find_all("td", {'align':'right'})[i + 2].text
    #     pricel.append(price)
    #     chngl.append(chng)
    #     pchngl.append(pchng)
    #     i += 4
    # while(i>=400 and i<600):
    #     price = soup.find_all("td", {'align':'right'})[i].text
    #     price = price.replace(',','')
    #     chng = soup.find_all("td", {'align':'right'})[i + 1].text
    #     pchng = soup.find_all("td", {'align':'right'})[i + 2].text
    #     pricel.append(price)
    #     chngl.append(chng)
    #     pchngl.append(pchng)
    #     i += 4
    # while (i >= 600 and i < 800):
    #     price = soup.find_all("td", {'align':'right'})[i].text
    #     price = price.replace(',','')
    #     chng = soup.find_all("td", {'align':'right'})[i + 1].text
    #     pchng = soup.find_all("td", {'align':'right'})[i + 2].text
    #     pricel.append(price)
    #     chngl.append(chng)
    #     pchngl.append(pchng)
    #     i += 4


def shownifty500(request):
    dbe = mysql.connect(host='localhost', port=3306, password='123', user='root', db='pgrdb')
    cmd = dbe.cursor()
    q = "select * from stocks500"
    cmd.execute(q)
    rec = cmd.fetchall()
    dbe.close()
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

