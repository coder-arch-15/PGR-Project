from django.contrib import admin
from .models import user
import sqlite3
# Register your models here.
admin.site.register(user)
conn = sqlite3.connect('pgr-database.db')
conn.execute('''CREATE TABLE IF NOT EXISTS USERS( username varchar(15) PRIMARY KEY NOT NULL, pasw VARCHAR NOT NULL, name varchar(30) NOT NULL,  email varchar(30) NOT NULL,  mob varchar(10) NOT NULL, plan varchar(10) NOT NULL,expiry TEXT(10) )''')
conn.execute('''CREATE TABLE IF NOT EXISTS USER_CASH( username varchar(15) PRIMARY KEY NOT NULL, cash VARCHAR(15) NOT NULL) ''')
conn.close()
 