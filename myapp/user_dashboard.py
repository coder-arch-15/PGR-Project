from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail
from django.conf import settings 
import sqlite3


def user_dashboard(request):
	if(request.session.has_key("username")):
		if( request.session['plan'] != "free"):
			print("hello")
			return render(request, "userdashboard.html")
		else:
			return render(request, "buymembershipp.html")
	else:
		return redirect("/login")


def user_show_stocks(request):
	if(request.session.has_key("username")):
		if( request.session['plan'] == "silver"):
			print("hello_show_stocks")
			return render(request, "usershowstocks.html")
		else:
			return render(request, "buymembershipp.html", {"error": "To access NIFTY-50 STOCKS section please activate SILVER or any premium plan!"})
	else:
		return redirect("/login")


def user_adv_stocks(request):
	if(request.session.has_key("username")):
		if( request.session['plan'] != "gold"):
			print("hello_adv_stocks")
			return render(request, "useradvstocks.html")
		else:
			return render(request, "buymembershipp.html", {"error": "To access ADVANCE STOCKS section please activate GOLD or any premium plan!"})
	else:
		return redirect("/login")


def user_analysis(request):
	if(request.session.has_key("username")):
		if( request.session['plan'] == "diamond"):
			print("hello_analysis")
			return render(request, "useranalysis.html")
		else:
			return render(request, "buymembershipp.html", {"error": "To access STOCKS ANALYSIS section please activate DIAMOND or any premium plan!"})
	else:
		return redirect("/login")


def user_watchlist(request):
	if(request.session.has_key("username")):
		if( request.session['plan'] == "silver"):
			print("hello_watchlist")
			return render(request, "userwatchlist.html")
		else:
			return render(request, "buymembershipp.html", {"error": "To access WATCHLIST section please activate SILVER or any premium plan!"})
	else:
		return redirect("/login")


def user_wallet(request):
	if(request.session.has_key("username")):
		if( request.session['plan'] == "silver"):
			print("hello_wallet")
			return render(request, "userwallet.html")
		else:
			return render(request, "buymembershipp.html", {"error": "To access WALLET section please activate SILVER or any premium plan!"})
	else:
		return redirect("/login")


def user_transaction(request):
	if(request.session.has_key("username")):
		if( request.session['plan'] == "silver"):
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
		if( request.session['plan'] == "silver"):
			print("hello_leaderboard")
			return render(request, "userleaderboard.html")
		else:
			return render(request, "buymembershipp.html", {"error": "To access LEADERBOARD section please activate SILVER or any premium plan!"})
	else:
		return redirect("/login")


def user_logout(request):
	try:
		del request.session['username']
		del request.session['plan']
	except:
		pass
	return redirect('/')