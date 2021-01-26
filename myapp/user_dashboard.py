from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail
from django.conf import settings 
import sqlite3


def user_dashboard(request):
	if(request.session.has_key("username")):
		if( int(request.session['plan']) != 0):
			print("hello")
			return render(request, "userdashboard.html")
		else:
			return render(request, "buymembershipp.html")
	else:
		return redirect("/login")


def user_show_stocks(request):
	if(request.session.has_key("username")):
		if( int(request.session['plan']) >= 1):
			print("hello_show_stocks")
			return render(request, "usershowstocks.html")
		else:
			return render(request, "buymembershipp.html", {"error": "To access NIFTY-50 STOCKS section please activate SILVER or any premium plan!"})
	else:
		return redirect("/login")


def user_adv_stocks(request):
	if(request.session.has_key("username")):
		if( int(request.session['plan']) >= 2):
			print("hello_adv_stocks")
			return render(request, "useradvstocks.html")
		else:
			return render(request, "buymembershipp.html", {"error": "To access ADVANCE STOCKS section please activate GOLD or any premium plan!"})
	else:
		return redirect("/login")


def user_analysis(request):
	if(request.session.has_key("username")):
		if( int(request.session['plan']) >= 3):
			print("hello_analysis")
			return render(request, "useranalysis.html")
		else:
			return render(request, "buymembershipp.html", {"error": "To access STOCKS ANALYSIS section please activate DIAMOND or any premium plan!"})
	else:
		return redirect("/login")


def user_watchlist(request):
	if(request.session.has_key("username")):
		if( int(request.session['plan']) >= 1):
			print("hello_watchlist")
			return render(request, "userwatchlist.html")
		else:
			return render(request, "buymembershipp.html", {"error": "To access WATCHLIST section please activate SILVER or any premium plan!"})
	else:
		return redirect("/login")


def user_wallet(request):
	if(request.session.has_key("username")):
		if( int(request.session['plan']) >= 1):
			print("hello_wallet")
			conn = sqlite3.connect('pgr-database.db')
			cur = conn.cursor()
			cur.execute("SELECT * FROM STOCKS")
			stocks = cur.fetchall()
			cur.execute("SELECT * FROM HOLDINGS WHERE username = ?", (request.session['username'],))
			table = cur.fetchall()
			conn.commit()
			conn.close()
			print("###############################")
			print(stocks)
			stocks[1][0]
			for user in table:
				stocks[int(user[3])][1]
			
			return render(request, "userwallet.html", {"table": table , "stocks": stocks})
		else:
			return render(request, "buymembershipp.html", {"error": "To access WALLET section please activate SILVER or any premium plan!"})
	else:
		return redirect("/login")


def user_transaction(request):
	if(request.session.has_key("username")):
		if( int(request.session['plan']) >= 1):
			print("hello_transaction")
			return render(request, "usertransaction.html")
		else:
			return render(request, "buymembershipp.html", {"error": "To access TRANSACTIONS section please activate SILVER or any premium plan!"})
	else:
		return redirect("/login")


def user_membership_account(request):
	if(request.session.has_key("username")):
		print("hello_account")
		return render(request, "useraccount.html")
	else:
		return redirect("/login")



def user_leaderboard(request):
	if(request.session.has_key("username")):
		if( int(request.session['plan']) >= 1):
			print("hello_leaderboard")
			return render(request, "userleaderboard.html")
		else:
			return render(request, "buymembershipp.html", {"error": "To access LEADERBOARD section please activate SILVER or any premium plan!"})
	else:
		return redirect("/login")


def user_buyplan(request,planid,expiry):
	if(request.session.has_key("username")):
		from datetime import datetime, timedelta
		planid = int(planid)

		if(expiry=="1"):
			expirydate = datetime.now() + timedelta(days=30) 
		elif(expiry=="2"):
			expirydate = datetime.now() + timedelta(days=90) 
		elif(expiry=="3"):
			expirydate = datetime.now() + timedelta(days=182) 
		elif(expiry=="4"):
			expirydate = datetime.now() + timedelta(days=365) 
		else:
			expirydate = ""
		conn = sqlite3.connect('pgr-database.db')
		cur = conn.cursor()
		cur.execute("UPDATE USERS SET plan = ?, pending = ?, approved = ?, expiry = ? WHERE username=?", (planid,1,0,expirydate,request.session['username']))
		conn.commit()
		conn.close()
		print("hello")
		request.session['plan'] = planid
		return redirect("/userdashboard")
	else:
		return redirect("/userlogout")


def user_logout(request):
	try:
		del request.session['username']
		del request.session['plan']
	except:
		pass
	return redirect('/')