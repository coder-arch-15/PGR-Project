from django.conf.urls import *
from myapp.views import *
from django.contrib import admin
from django.urls import path
admin.autodiscover()

urlpatterns = [
	path("", home, name = 'home'),
    path("admin/", admin.site.urls),
    path("register", register, name = 'register' ),
    path("reg_submit", register_check, name = 'register_check' ),
    path('login', user_login, name = 'user_login' ),
    path("adminlogin", admin_login, name = 'admin_login' ),
    path("userlogout", user_logout, name = 'user_logout' ),
    path("usrloginsubmit", user_login_submit, name = 'user_login_submit' ),
    path("admloginsubmit", admin_login_submit, name = 'admin_login_submit' ),
    path("admindashboard/", admin_dashboard, name = 'admin_dashboard' ),
    path("userdashboard", user_dashboard, name = 'user_dashboard' ),
    url(r'^adminreject/(\d+)/', reject, name = 'reject'),
    url(r'^adminaccept/(\d+)/', accept, name = 'accept'),
]