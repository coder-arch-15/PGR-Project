from django.conf.urls import *
from myapp.views import *
from myapp.user_dashboard import *
from django.contrib import admin
from django.urls import path
from . import User
from . import UserLogin
from . import Admin
from . import Nifty50
from . import Nifty500
from . import tempnifty500
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
    path('updatepriceaction', updatepriceaction,name = 'updatepriceaction'),
    path('updateindices', updateIndices,name = 'updateIndices'),
    path('updateallindices', updateAllIndices,name = 'updateAllIndices'),
    path('allindices', all_indices ,name = 'all_indices'),

    # url(r'^updatestockinfo/(?P<ticker>[\D\-]+)/$', updateStockInfo, name = 'updateStockInfo'),
    path('updatestockinfo/', updateStockInfo, name = 'updateStockInfo'),

    path("buyplanpage/", buyplanpage, name = 'buyplanpage' ),
    path("usershowstocks", user_show_stocks, name = 'user_show_stocks' ),
    path("useradvstocks", user_adv_stocks, name = 'user_adv_stocks' ),
    path("userwatchlist", user_watchlist, name = 'user_watchlist' ),
    path("usertransaction", user_transaction, name = 'user_transaction' ),
    path("useranalysis", user_analysis, name = 'user_analysis' ),
    path("userwallet", user_wallet, name = 'user_wallet' ),
    path("userleaderboard", user_leaderboard, name = 'user_leaderboard' ),
    path("usermembershipaccount", user_membership_account, name = 'user_membership_account' ),
    url(r'^buyplan/(\d+)/(\d+)/', user_buyplan, name = 'user_buyplan'),
    path("stockpage/", stockpage, name = 'stockpage' ),
    path("indexpage/", index_page, name = 'index_page' ),
    path("updateindexpage/", update_index_page, name = 'update_index_page' ),
    path("advstockchart/", advanceStockChart, name = 'advanceStockChart' ),


    path('user/', User.ActionUserInterface),
    path('usersubmit', User.ActionUserSubmit),
    path('userlogin/', UserLogin.ActionUserLogin),
    path('checkuser', UserLogin.ActionCheckUserLogin),
    path('logout/', Admin.ActionLogout),
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
    path('shownifty50/',Nifty50.ActionShowNifty50),
    path('updateshownifty50',updateshownifty50),
    path('update1shownifty500',Nifty500.update1shownifty500),
    path('update2shownifty500',Nifty500.update2shownifty500),
    path('shownifty500/',Nifty500.shownifty500),
    path('shownifty500temp',tempnifty500.tempshownifty500),
    path('tempupdateshownifty500',tempnifty500.tempupdateshownifty500),

]



urlpatterns+=staticfiles_urlpatterns()
#test2