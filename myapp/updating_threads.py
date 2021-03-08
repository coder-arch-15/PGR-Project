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


def updateAllIndicesThread():	#returns indices data
	while(True):
		try:
			url = requests.get('https://www.moneycontrol.com/markets/irol.com/markets/indian-indices/?classic=true', timeout=5)
			soup = bs4.BeautifulSoup(url.text, features="html.parser")
			i = 0
			pricel=[]
			chngl=[]
			pchngl=[]
			res = soup.find_all("td", {'align': 'right'})
			for i in range(70):
				if (i==1 or ((i>39) and (i<63))):
					pricel.append(res[6*i].text.replace(',',''))
					chngl.append(res[6*i+1].text)
					pchngl.append(res[6*i+2].text)
			data.allIndices = {"price":pricel, "chng": chngl, "pchng":pchngl} 
		
			if (datetime.datetime.now()>end_time) or (datetime.datetime.now()<start_time) or (datetime.datetime.now().strftime("%A")=="Saturday") or (datetime.datetime.now().strftime("%A")=="Sunday"):
				break
			time.sleep(5)
		except:
			pass


def updateshownifty50Thread():
	while(True):
		
		try:
		    url = requests.get(
		        'https://www.moneycontrol.com/stocks/marketstats/indexcomp.php?optex=NSE&opttopic=indexcomp&index=9')
		    soup = bs4.BeautifulSoup(url.text, features="html.parser")
		    tickers = []
		    i = 0
		    pricel=[]
		    chngl=[]
		    pchngl=[]
		    res = soup.find_all("td", {'align': 'right'})
		    while (i < 200):
		    	pricel.append(res[i].text.replace(',',''))
		    	chngl.append(res[i + 1].text)
		    	pchngl.append(res[i + 2].text)
		    	i += 4
		    data.nifty50data = {"price":pricel, "chng": chngl, "pchng":pchngl} 
		except:
			pass
		if (datetime.datetime.now()>end_time) or (datetime.datetime.now()<start_time) or (datetime.datetime.now().strftime("%A")=="Saturday") or (datetime.datetime.now().strftime("%A")=="Sunday"):
			break
		time.sleep(40)	    


def updateshownifty500Thread():
	while(True):
		url = requests.get('https://www.moneycontrol.com/stocks/marketstats/indexcomp.php?optex=NSE&opttopic=indexcomp&index=7')
		soup = bs4.BeautifulSoup(url.text, features="html.parser")
		res = soup.find_all("td", {"class":"brdrgtgry"})
		try:
			tempdata = []
			i = 0
			while (i<2929):
				tempdata.append({"ticker":res[i].text.split("\n")[0],
				 "price":res[i+2].text,
				  "chng": res[i+3].text,
				   "pchng":res[i+4].text})
				i += 6
			
			data.nifty500data=tempdata
			if (datetime.datetime.now()>end_time) or (datetime.datetime.now()<start_time) or (datetime.datetime.now().strftime("%A")=="Saturday") or (datetime.datetime.now().strftime("%A")=="Sunday"):
				break
		except:
			pass
		time.sleep(40)
      

def update_data(): 
	t2 = threading.Thread(target=updateAllIndicesThread,daemon=True) 
	t3 = threading.Thread(target=updateshownifty500Thread,daemon=True) 
	t5 = threading.Thread(target=updateshownifty50Thread,daemon=True) 

	t5.start()
	t3.start()
	t2.start()
	return
  

# def updateIndicesThread():
# 	while(True):
# 		time.sleep(3)
# 		try:
# 			url = requests.get('https://www.moneycontrol.com/markets/irol.com/markets/indian-indices/?classic=true', timeout=5)
# 			soup = bs4.BeautifulSoup(url.text, features="html.parser")
# 			res = soup.find_all("td", {'align': 'right'})
# 			data.indices = {
# 	        "NIFTY50":res[6].text ,
# 	        "NIFTY50CHNG":res[7].text,
# 	        "NIFTY50PCHNG":res[8].text,
# 	        "NIFTYBANK":res[276].text,
# 	        "NIFTYBANKCHNG":res[277].text,
# 	        "NIFTYBANKPCHNG":res[278].text,
# 	        "NIFTYENERGY":res[294].text,
# 	        "NIFTYENERGYCHNG":res[295].text,
# 	        "NIFTYENERGYPCHNG":res[296].text,
# 	        "NIFTYIT":res[318].text,
# 	        "NIFTYITCHNG":res[319].text,
# 	        "NIFTYITPCHNG":res[320].text
# 	        }
# 		except Exception as e:
# 			pass
# 		if (datetime.datetime.now()>end_time) or (datetime.datetime.now()<start_time):
# 			break