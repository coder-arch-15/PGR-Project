from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings 
import pymysql
from yahoo_finance import Share


def get_cmp(request, ticker):
	print(ticker)
	temp = Share(ticker)
	print(temp.get_open())
	pass