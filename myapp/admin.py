from django.contrib import admin
from .models import user
import pymysql 
from . import updating_threads as ut

ut.update_data()


# conn = pymysql.connect( 
#         host='localhost',
# 		port =3306 ,
#         user='root',  

#         password = "123",
#         db='pgrdb',
#         ) 
# cursor = conn.cursor()
# cursor.execute('''CREATE TABLE IF NOT EXISTS USERS( username varchar(15) PRIMARY KEY NOT NULL, pasw VARCHAR(15) NOT NULL, name varchar(30) NOT NULL,  email varchar(30) NOT NULL,  mob varchar(10) NOT NULL, plan varchar(10) NOT NULL,expiry TEXT(10), pending int NOT NULL, approved INT NOT NULL, cash FLOAT default 1000000 )''')
# cursor.execute('''CREATE TABLE IF NOT EXISTS ORDERS ( username varchar(15) NOT NULL, date VARCHAR(25) NOT NULL, company VARCHAR(15) NOT NULL, quantity FLOAT(10) NOT NULL, tp FLOAT(8) NOT NULL, TTYPE TEXT(4), STATUS VARCHAR (20) )''')
# cursor.execute('''CREATE TABLE IF NOT EXISTS HOLDINGS( username varchar(15) NOT NULL, quantity FLOAT(10) NOT NULL, tp FLOAT(5) NOT NULL, COMPANY VARCHAR(15) NOT NULL, TOTAL FLOAT(15) NOT NULL) ''')
# cursor.execute('''CREATE TABLE IF NOT EXISTS STOCKS( COMPANY varchar(15) PRIMARY KEY NOT NULL, CMP FLOAT(5) NOT NULL, OPEN FLOAT(5) NOT NULL, CLOSE FLOAT(5) NOT NULL, LOW FLOAT(5) NOT NULL, HIGH FLOAT(5) NOT NULL,COMPANY_NAME VARCHAR(100) NOT NULL, symbol VARCHAR(35), bsecode INT) ''')



# ########################## Uncomment this part to add few entries in table################################


# cursor.execute(''' INSERT INTO HOLDINGS VALUES("aa", 100, 15, "ADANIPORTS.NS", 1500)  ''')
# cursor.execute(''' INSERT INTO HOLDINGS VALUES("aa", 200, 150, "BAJAJFINSV.NS", 30000)  ''')
# cursor.execute(''' INSERT INTO HOLDINGS VALUES("aa", 100, 150, "MSFT", 15000)  ''')

# import bs4
# import requests
# from bs4 import BeautifulSoup
# url = requests.get('https://en.wikipedia.org/wiki/NIFTY_50')
# soup = bs4.BeautifulSoup(url.text, features="html.parser")
# i=39
# while(i<150):
# 	ticker = soup.find_all("table", {'id': 'constituents'})[0].find_all('td')[i+1].text
# 	companyname = soup.find_all("table", {'id': 'constituents'})[0].find_all('td')[i].text
# 	companyname+=" Limited"
# 	i+=3
# 	print("Tick = "+ticker+" companyname =" +companyname)
# 	q= "INSERT INTO STOCKS(company,cmp,open,close,high,low,COMPANY_NAME) VALUES('{0}', 0, 0, 0 , 0, 0, '{1}')".format(ticker,companyname)
# 	cursor.execute(q)
# 	conn.commit()

###############################adding symbol names to the table#####################
# x = ['Adani Ports SEZ', 'Asian Paints', 'Axis Bank', 'BPCL', 'Bajaj Auto', 'Bajaj Finance', 'Bajaj Finserv', 'Bharti Airtel', 'Britannia Inds.', 'Cipla', 'Coal India Ltd', 'Divis Labs', 'Dr. Reddys', 'Eicher Motors', 'GAIL', 'Grasim Inds.', 'HCL Tech', 'HDFC', 'HDFC Bank', 'HDFC Life', 'Hero MotoCorp', 'Hind. Unilever', 'Hindalco Inds.', 'ICICI Bank', 'ITC', 'Indian Oil Corp', 'IndusInd Bank', 'Infosys', 'JSW Steel', 'Kotak Bank', 'Larsen & Toubro', 'M&M', 'Maruti Suzuki', 'NTPC', 'Nestle India', 'ONGC', 'PowerGrid', 'RIL', 'SBI', 'SBI Life', 'Shree Cements', 'Sun Pharma', 'TCS', 'Tata Motors', 'Tata Steel', 'Tech Mahindra', 'Titan Company ', 'UPL ', 'UltraTech Cem.', 'Wipro']
# y = ['ADANIPORTS.NS', 'ASIANPAINT.NS', 'AXISBANK.NS', 'BAJAJ-AUTO.NS', 'BAJAJFINSV.NS', 'BAJFINANCE.NS', 'BHARTIARTL.NS', 'BPCL.NS', 'BRITANNIA.NS', 'CIPLA.NS', 'COALINDIA.NS', 'DIVISLAB.NS', 'DRREDDY.NS', 'EICHERMOT.NS', 'GAIL.NS', 'GRASIM.NS', 'HCLTECH.NS', 'HDFC.NS', 'HDFCBANK.NS', 'HDFCLIFE.NS', 'HEROMOTOCO.NS', 'HINDALCO.NS', 'HINDUNILVR.NS', 'ICICIBANK.NS', 'INDUSINDBK.NS', 'INFY.NS', 'IOC.NS', 'ITC.NS', 'JSWSTEEL.NS', 'KOTAKBANK.NS', 'LT.NS', 'M&M.NS', 'MARUTI.NS', 'NESTLEIND.NS', 'NTPC.NS', 'ONGC.NS', 'POWERGRID.NS', 'RELIANCE.NS', 'SBILIFE.NS', 'SBIN.NS', 'SHREECEM.NS', 'SUNPHARMA.NS', 'TATAMOTORS.NS', 'TATASTEEL.NS', 'TCS.NS', 'TECHM.NS', 'TITAN.NS', 'ULTRACEMCO.NS', 'UPL.NS', 'WIPRO.NS']
# security_code = [532921, 500820, 532215, 532977, 532978, 500034, 532454, 500547, 500825, 500087, 533278, 532488, 500124, 505200, 532155, 500300, 532281, 500010, 500180, 540777, 500182, 500440, 500696, 532174, 532187, 500209, 530965, 500875, 500228, 500247, 500510, 500520, 532500, 500790, 532555, 500312, 532898, 500325, 540719, 500112, 500387, 524715, 500570, 500470, 532540, 532755, 500114, 532538, 512070, 507685]

# for tick,cname in zip(y,x):
# 	q = "UPDATE STOCKS SET symbol = '{0}' WHERE COMPANY = '{1}'".format(cname, tick)
# 	cursor.execute(q)
# 	conn.commit()

# for tick,code in zip(y,security_code):
# 	q = "UPDATE STOCKS SET bsecode = '{0}' WHERE COMPANY = '{1}'".format(code, tick)
# 	cursor.execute(q)
# 	conn.commit()

###############################################################


# conn.commit()
# conn.close()