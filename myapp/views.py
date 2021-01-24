from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import Register, loginForm
from .models import user
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings 
import sqlite3

def home(request):
	if(request.session.has_key("username")):
		return redirect("/userdashboard")
	return render(request, "home.html")

def register(request):
	return render(request, "userregister.html")

    
def user_login(request):
	if(request.session.has_key("username")):
		return redirect("/userdashboard")
	return render(request, "userlogin.html")

def user_login_submit(request):
	if(request.session.has_key("username")):
		return redirect("/userdashboard")
	else:
		if (request.method == 'POST'):
			username = str(request.POST['username'])
			password = request.POST['password']
			conn = sqlite3.connect('pgr-database.db')
			cur = conn.cursor()
			cur.execute("SELECT pasw,plan FROM users WHERE username=?", (username,))
			user,plan = cur.fetchone()
			conn.commit()
			conn.close()
			if user is not None:
				request.session['username'] = username
				request.session['plan'] = plan
				return redirect("/userdashboard")
			else:
				return render(request, "userlogin.html", {"error": "Invalid username or password!"} )
	
		return redirect("/login")


def check_username_exist(request):
	username=request.POST.get("user_login-25")
	name=request.POST.get("nickname-25")
	email=request.POST.get("user_email-25")
	mob=request.POST.get("mobile_number-25")
	pasw=request.POST.get("user_password-25")
	conn = sqlite3.connect('pgr-database.db')
	cur = conn.cursor()
	cur.execute("SELECT * FROM users WHERE username=?", (username,))
	user_obj = cur.fetchall()
	free = "free"
	if user_obj:
		conn.close()
		return render(request, "userregister.html", {"error" : "Username - '"+username+"' is not available!" , "name":name, "email": email, "mob":mob})
	else:
		cur.execute("insert into users (username,pasw,name,email, mob,plan,pending,approved) values(?,?,?,?,?,?,?,?)",(username, pasw, name,email,mob,free,1,0))
		conn.commit()
		cur.execute("insert into user_cash (username,cash) values (?,?)", (username, 1000000))
		conn.commit()
		conn.close()
		return redirect("/")


def admin_dashboard(request):
	objects = user.objects.all()
	res =[]
	return render(request, "admin_dashboard.html",{"table" : objects})


def admin_login(request):
	context ={}
	context['form']= loginForm()
	return render(request, "adminlogin.html", context)


def admin_login_submit(request):
	username = request.POST['username']
	password = request.POST['password']
	if(username=="admin" and password=="1234"):
		return redirect("/admindashboard/")

	return redirect("admin_login")


def accept(request, userid):
   userId = user.objects.get(id = userid)
   userId.pending = 0;
   userId.approved = 1;
   userId.save()
   subject = 'PGR Registration Accepted'
   message = f'Hi {userId.name}, thank you for registering in Praedico Global Research. Your registration has been approved! Please login with your email as Username and default password is "1234test".'
   email_from = settings.EMAIL_HOST_USER 
   recipient_list = [userId.mail] 
   send_mail( subject, message, email_from, recipient_list ) 
   return redirect("/admindashboard/")

def reject(request, userid):
   userId = user.objects.get(id = userid)
   userId.pending = 0;
   userId.approved = 0;
   userId.save()
   subject = 'PGR Registration '
   message = f'Hi {userId.name}, your registration has been declined by the Admin! Kindly contact at "admin.pgr@gmail.com" for further information.'
   email_from = settings.EMAIL_HOST_USER 
   recipient_list = [userId.mail] 
   send_mail( subject, message, email_from, recipient_list ) 
   return redirect("/admindashboard/")