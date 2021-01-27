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
cursor.execute('''CREATE TABLE IF NOT EXISTS STOCKS( COMPANY varchar(15) PRIMARY KEY NOT NULL, CMP FLOAT(5) NOT NULL, OPEN FLOAT(5) NOT NULL, CLOSE FLOAT(5) NOT NULL, LOW FLOAT(5) NOT NULL, HIGH FLOAT(5) NOT NULL,  CHNG FLOAT(5) NOT NULL) ''')
cursor.execute(''' INSERT INTO HOLDINGS VALUES("aa", 100, 15, 0, 1500)  ''')
# cursor.execute(''' INSERT INTO HOLDINGS VALUES("aa", 200, 150, 1, 30000)  ''')
# cursor.execute(''' INSERT INTO HOLDINGS VALUES("aa", 100, 150, 2, 15000)  ''')
# cursor.execute(''' INSERT INTO STOCKS VALUES("IDEA", 11.75, 15, 20, 21, 13, 20.5)  ''')
# cursor.execute(''' INSERT INTO STOCKS VALUES("MOTHERSUN", 175, 15, 20, 21, 13, 20.5)  ''')
# cursor.execute(''' INSERT INTO STOCKS VALUES("RIL", 2000, 15, 20, 21, 13, 20.5)  ''')
# cursor.execute(''' INSERT INTO STOCKS VALUES("ADANI", 100, 15, 20, 21, 13, 20.5)  ''')
conn.commit()
conn.close()