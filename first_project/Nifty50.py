from django.shortcuts import render,redirect
import pymysql as mysql
import bs4
import requests
from bs4 import BeautifulSoup
from difflib import get_close_matches
import time
starttime=time.time()


def ActionShowNifty50(request):
    if(request.session.has_key("user")):
        if( int(request.session['user'][5]) != 0):
            dbe = mysql.connect(host='localhost', port=3306, password='123', user='root', db='pgrdb')
            cmd = dbe.cursor()
            q = "select * from stocks"
            cmd.execute(q)
            rec = cmd.fetchall()
            dbe.close()
            return render(request,"tempnifty50.html",{'stocks':rec})
        else:
            return redirect("/buyplanpage")
    else:
        return redirect("/login")


def ActionBuySellForm(request):
    return render(request, "buysellform.html")
