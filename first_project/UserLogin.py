from django.shortcuts import render
import pymysql as mysql
from django.contrib import auth

def ActionUserLogin(request):
    return render(request,"NewUserLogin.html",{"msg":''})
def ActionCheckUserLogin(request):
    try:
      userid=request.POST['adminId']
      password=request.POST['password']
      dbe = mysql.connect(host='localhost', port=3306, password='123', user='root', db='dummy')
      cmd = dbe.cursor()
      q="select * from user where userid='{0}' and password='{1}' and adminact='Approved'".format(userid,password)
      cmd.execute(q)
      rec=cmd.fetchone()
      if(rec):
        return render(request,"Dashboard.html",{'admin':rec})
      else:
        return render(request, "NewUserLogin.html",{'msg':'Invalid UserId/Password or Your registration is not approved from admin'})
    except Exception as e:
        print(e)
        return render(request, "NewUserLogin.html",{'msg':'Server Error'})

def ActionLogout(request):
    auth.logout(request)
    return render(request,"NewUserLogin.html",{'msg':[]})