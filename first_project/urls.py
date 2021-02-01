from django.conf.urls import *
from myapp.views import *
from myapp.user_dashboard import *
from django.contrib import admin
from django.urls import path
from . import User
from . import UserLogin
from . import Admin
from myapp.stock_data import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
admin.autodiscover()

urlpatterns = [
	path("", home, name = 'home'),
    path("admin/", admin.site.urls),
    path("register", register, name = 'register' ),
    path('login', user_login, name = 'user_login' ),
    path("adminlogin", admin_login, name = 'admin_login' ),
    path("userlogout", user_logout, name = 'user_logout' ),
    path("userloginsubmit", user_login_submit, name = 'user_login_submit' ),
    path("adminloginsubmit", admin_login_submit, name = 'admin_login_submit' ),
    path("admindashboard/", admin_dashboard, name = 'admin_dashboard' ),
    path("userdashboard", user_dashboard, name = 'user_dashboard' ),
    url(r'^adminreject/(\d+)/', reject, name = 'reject'),
    url(r'^adminaccept/(\d+)/', accept, name = 'accept'),
    path('check_username_exist', check_username_exist, name = 'check_username_exist'),
    url(r'^getcmp/(?P<ticker>[\D\-]+)/$', getcmp, name = 'getcmp'),
    path('updatecmp', updatecmp,name = 'updatecmp'),
    path('user/', User.ActionUserInterface),
    path('usersubmit', User.ActionUserSubmit),
 
    path("buyplanpage", buyplanpage, name = 'buyplanpage' ),
    path("usershowstocks", user_show_stocks, name = 'user_show_stocks' ),
    path("useradvstocks", user_adv_stocks, name = 'user_adv_stocks' ),
    path("userwatchlist", user_watchlist, name = 'user_watchlist' ),
    path("usertransaction", user_transaction, name = 'user_transaction' ),
    path("useranalysis", user_analysis, name = 'user_analysis' ),
    path("userwallet", user_wallet, name = 'user_wallet' ),
    path("userleaderboard", user_leaderboard, name = 'user_leaderboard' ),
    path("usermembershipaccount", user_membership_account, name = 'user_membership_account' ),
    url(r'^buyplan/(\d+)/(\d+)/', user_buyplan, name = 'user_buyplan'),





    path('userlogin/', UserLogin.ActionUserLogin),
    path('checkuser', UserLogin.ActionCheckUserLogin),
    path('logout/', UserLogin.ActionLogout),
    path('displayalluserlogin/', User.ActionDisplayAllUserLogin),
    path('userdisplaybyidlogin/', User.ActionDisplayByIdLogin),
    path('usereditdeletesubmitlogin', User.ActionUserEditDeleteSubmitLogin),
    path('adminlogin/',Admin.ActionAdminLogin),
    path('checkadmin', Admin.ActionCheckAdminLogin),
    path('displayalluser/', Admin.ActionDisplayAllUser),
    path('userdisplaybyid/', Admin.ActionDisplayById),
    path('admineditdeletesubmit', Admin.ActionAdminEditDeleteSubmit),
    path('userregister/',User.ActionUserInterface),
    path('usersubmit', User.ActionUserSubmit),

]



urlpatterns+=staticfiles_urlpatterns()
#test2