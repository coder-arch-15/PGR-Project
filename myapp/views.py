from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import Register, loginForm
from .models import user
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings 

def home(request):
   return render(request, "home2.html")

def register(request):
	context ={}
	context['form']= Register()
	return render(request, "register.html", context)


def register_check(request): 
    context ={} 
  
    # create object of form 
    form = Register(request.POST or None, request.FILES or None) 
      

    if form.is_valid():
            # process form data
            form.save() 
            return HttpResponseRedirect('/')
    
def user_login(request):
	context ={}
	context['form']= loginForm()
	return render(request, "userlogin.html", context)

def user_login_submit(request):
	# if request.user.is_authenticated:
	# 	return redirect("/userdashboard/")
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		users = user.objects.filter(mail = username).filter(password = password).first()

		if users is not None:
		    request.session['username'] = username
		    return render(request, "user_dashboard.html")
		else:
			context ={}
			context['form']= loginForm()
			return redirect("/userlogin")
	
	return redirect("/")


@login_required
def user_dashboard(request):
	
	return render(request, "user_dashboard.html")

@login_required
def user_logout(request):
	try:
		del request.session['username']
	except:
		pass
	return redirect('/')


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