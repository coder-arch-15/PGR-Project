from django.contrib import admin
from .models import user
import pymysql 
conn = pymysql.connect( 
        host='localhost',
		port =3306 ,
        user='root',  
        password = "1234", 
        db='pgrdb', 
        ) 
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS USERS( username varchar(15) PRIMARY KEY NOT NULL, pasw VARCHAR(15) NOT NULL, name varchar(30) NOT NULL,  email varchar(30) NOT NULL,  mob varchar(10) NOT NULL, plan varchar(10) NOT NULL,expiry TEXT(10), pending int NOT NULL, approved INT NOT NULL )''')
cursor.execute('''CREATE TABLE IF NOT EXISTS USER_CASH( username varchar(15) PRIMARY KEY NOT NULL, cash VARCHAR(15) NOT NULL) ''')
cursor.execute('''CREATE TABLE IF NOT EXISTS TRANS ( username varchar(15) NOT NULL, tid varchar(10) NOT NULL, date TEXT(10) NOT NULL, company INT NOT NULL, quantity FLOAT(6) NOT NULL, tp FLOAT(7) NOT NULL, TTYPE TEXT(4), TOTAL FLOAT(12) NOT NULL, comment VARCHAR (50) )''')
cursor.execute('''CREATE TABLE IF NOT EXISTS HOLDINGS( username varchar(15) NOT NULL, quantity FLOAT(10) NOT NULL, tp FLOAT(5) NOT NULL, COMPANY INT NOT NULL, TOTAL FLOAT(15) NOT NULL) ''')
cursor.execute('''CREATE TABLE IF NOT EXISTS STOCKS( COMPANY varchar(15) PRIMARY KEY NOT NULL, CMP FLOAT(5) NOT NULL, OPEN FLOAT(5) NOT NULL, CLOSE FLOAT(5) NOT NULL, LOW FLOAT(5) NOT NULL, HIGH FLOAT(5) NOT NULL,COMPANY_NAME VARCHAR(35) NOT NULL) ''')



# ########################## Uncomment this part to add few entries in table################################

# cursor.execute(''' INSERT INTO HOLDINGS VALUES("aa", 100, 15, 0, 1500)  ''')
# cursor.execute(''' INSERT INTO HOLDINGS VALUES("aa", 200, 150, 1, 30000)  ''')
# cursor.execute(''' INSERT INTO HOLDINGS VALUES("aa", 100, 150, 2, 15000)  ''')
# import bs4
# import requests
# from bs4 import BeautifulSoup 
# url = requests.get('https://finance.yahoo.com/quote/%5ENSEI/components?p=%5ENSEI')
# soup = bs4.BeautifulSoup(url.text, features="html.parser")
# for i in range(30):
# 	ticker = soup.find_all("tr", {'class': 'BdT Bdc($seperatorColor) Ta(end) Fz(s)'})[i].text
# 	tick,cname = ticker.split(".NS")
# 	tick="'"+tick+".NS'"
# 	companyname,remaining = cname.split("Limited")
# 	companyname="'"+companyname+"Limited'"
# 	print(tick)
# 	print(companyname)
# 	q= "INSERT INTO STOCKS(company,cmp,open,close,high,low,CHNG,COMPANY_NAME) VALUES({0}, 0, 0, 0,0 , 0, 0, {1})".format(tick,companyname)
# 	print(q)
# 	cursor.execute(q)
# 	conn.commit()
###############################################################

conn.commit()
conn.close()