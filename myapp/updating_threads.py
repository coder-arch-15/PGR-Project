import threading 
import time
import datetime
from . import data
import bs4
import requests
from bs4 import BeautifulSoup 

now = datetime.datetime.now()
start_time = now.replace(hour=9, minute=15, second=0, microsecond=0)
end_time = now.replace(hour=15, minute=30, second=0, microsecond=0)


def updateIndicesThread():
	while(True):
		time.sleep(2)
		try:
			url = requests.get('https://www.moneycontrol.com/markets/irol.com/markets/indian-indices/?classic=true', timeout=5)
			soup = bs4.BeautifulSoup(url.text, features="html.parser")
			data.indices = {
	        "NIFTY50":soup.find_all("td", {'align': 'right'})[6].text ,
	        "NIFTY50CHNG":soup.find_all("td", {'align': 'right'})[7].text,
	        "NIFTY50PCHNG":soup.find_all("td", {'align': 'right'})[8].text,
	        "NIFTYBANK":soup.find_all("td", {'align': 'right'})[276].text,
	        "NIFTYBANKCHNG":soup.find_all("td", {'align': 'right'})[277].text,
	        "NIFTYBANKPCHNG":soup.find_all("td", {'align': 'right'})[278].text,
	        "NIFTYENERGY":soup.find_all("td", {'align': 'right'})[294].text,
	        "NIFTYENERGYCHNG":soup.find_all("td", {'align': 'right'})[295].text,
	        "NIFTYENERGYPCHNG":soup.find_all("td", {'align': 'right'})[296].text,
	        "NIFTYIT":soup.find_all("td", {'align': 'right'})[318].text,
	        "NIFTYITCHNG":soup.find_all("td", {'align': 'right'})[319].text,
	        "NIFTYITPCHNG":soup.find_all("td", {'align': 'right'})[320].text
	        }
		except Exception as e:
			pass
		if (datetime.datetime.now()>end_time) or (datetime.datetime.now()<start_time):
			break


def updateAllIndicesThread():	#returns indices data
	while(True):
		time.sleep(2)
		try:
			url = requests.get('https://www.moneycontrol.com/markets/irol.com/markets/indian-indices/?classic=true', timeout=5)
			soup = bs4.BeautifulSoup(url.text, features="html.parser")
			i = 0
			pricel=[]
			chngl=[]
			pchngl=[]
			for i in range(70):
				if (i==1 or ((i>39) and (i<63))):
					price = soup.find_all("td", {'align': 'right'})[6*i].text
					price=price.replace(',','')
					price = float(price)
					chng = soup.find_all("td", {'align': 'right'})[6*i+1].text
					pchng = soup.find_all("td", {'align': 'right'})[6*i+2].text
					pricel.append(price)
					chngl.append(chng)
					pchngl.append(pchng)
			data.data = {"price":pricel, "chng": chngl, "pchng":pchngl} 
		except:
			pass
		if (datetime.datetime.now()>end_time) or (datetime.datetime.now()<start_time):
			break


def updateshownifty50Thread():
	while(True):
		time.sleep(1)
		try:
		    url = requests.get(
		        'https://www.moneycontrol.com/stocks/marketstats/indexcomp.php?optex=NSE&opttopic=indexcomp&index=9')
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
		    data.nifty50data = {"price":pricel, "chng": chngl, "pchng":pchngl} 
		except:
			pass
		if (datetime.datetime.now()>end_time) or (datetime.datetime.now()<start_time):
			break		    


def updateshownifty500Thread():
	url = requests.get('https://www.moneycontrol.com/stocks/marketstats/indexcomp.php?optex=NSE&opttopic=indexcomp&index=7')
	soup = bs4.BeautifulSoup(url.text, features="html.parser")
	while(True):
		try:
			tempdata = []
			tickers = []
			i = 0
			pricel=[]
			chngl=[]
			pchngl=[]
			try:
				while(True):
					ticker = soup.find_all("td", {"class":"brdrgtgry"})[i].text.split("\n")[0]
					industry = soup.find_all("td", {"class":"brdrgtgry"})[i+1].text
					price = soup.find_all("td", {"class":"brdrgtgry"})[i+2].text
					price = price.replace(',','')
					chng = soup.find_all("td", {"class":"brdrgtgry"})[i+3].text
					pchng = soup.find_all("td", {"class":"brdrgtgry"})[i+4].text
					i += 6
					tempdata.append({"ticker":ticker, "price":price, "chng": chng, "pchng":pchng})

			except:
				data.nifty500data=tempdata
		except:
			pass
		if (datetime.datetime.now()>end_time) or (datetime.datetime.now()<start_time):
			break
      

def update_data(): 
	t1 = threading.Thread(target=updateIndicesThread,daemon=True) 
	t2 = threading.Thread(target=updateAllIndicesThread,daemon=True) 
	t3 = threading.Thread(target=updateshownifty50Thread,daemon=True) 
	t4 = threading.Thread(target=updateshownifty500Thread,daemon=True) 
	t4.start()
	t3.start()
	t2.start()
	t1.start() 
	return
  