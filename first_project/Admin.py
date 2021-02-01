from django.shortcuts import render
import pymysql as mysql
from django.contrib import auth
from django.views.decorators.clickjacking import xframe_options_exempt

def ActionAdminLogin(request):
    return render(request,"AdminLogin.html",{"msg":''})
def ActionCheckAdminLogin(request):
    try:
      adminid=request.POST['adminId']
      password=request.POST['password']
      dbe = mysql.connect(host='localhost', port=3306, password='123', user='root', db='dummy')
      cmd = dbe.cursor()
      q="select * from admin where adminid='{0}' and password='{1}'".format(adminid,password)
      cmd.execute(q)
      rec=cmd.fetchone()
      if(rec):
        return render(request,"AdminDashboard.html",{'admin':rec})
      else:
        return render(request, "AdminLogin.html",{'msg':'Invalid UserId/Password or Your registration is not approved from admin'})
    except Exception as e:
        print(e)
        return render(request, "AdminLogin.html",{'msg':'Server Error'})

@xframe_options_exempt
def ActionDisplayAllUser(request):
    try:

     dbe = mysql.connect(host='localhost', port=3306, password='123', user='root', db='pgrdb')
     cmd = dbe.cursor()
     q = "select * from users"
     cmd.execute(q)
     rows=cmd.fetchall()
     dbe.close()
     return render(request,"AdminDisplayAll.html",{"rows":rows})
    except Exception as e:
        print(e)
        return render(request, "AdminDisplayAll.html", {"rows":[]})

@xframe_options_exempt
def ActionDisplayById(request):
    try:
     ccid=request.GET['ccid']
     dbe = mysql.connect(host='localhost', port=3306, password='123', user='root', db='pgrdb')
     cmd = dbe.cursor()
     q = "select * from users where username={0}".format(ccid)
     cmd.execute(q)
     row=cmd.fetchone()
     dbe.close()
     return render(request,"AdminDisplayById.html",{"row":row})
    except Exception as e:
        print(e)
        return render(request, "AdminDisplayById.html", {"row":[]})

@xframe_options_exempt
def ActionAdminEditDeleteSubmit(request):
        ccid=request.POST['ccid']
        btn=request.POST['btn']
        try:
         if(btn=='Pending'):
          dbe=mysql.connect(host='localhost',port=3306,password='123',user='root',db='pgrdb')
          cmd=dbe.cursor()
          q="update users set approved='{0}' where username='{1}'".format(0,ccid)
          cmd.execute(q)
          dbe.commit()
          dbe.close()
          return ActionDisplayAllUser(request)
         elif(btn=='Approved'):
             dbe = mysql.connect(host='localhost', port=3306, password='123', user='root', db='pgrdb')
             cmd = dbe.cursor()
             q = "update users set approved='{0}' where username='{1}'".format(1,ccid)
             cmd.execute(q)
             dbe.commit()
             dbe.close()
             return ActionDisplayAllUser(request)
         elif (btn == 'DisApproved'):
             dbe = mysql.connect(host='localhost', port=3306, password='123', user='root', db='pgrdb')
             cmd = dbe.cursor()
             q = "update users set approved='{0}' where username='{1}'".format(0,ccid)
             cmd.execute(q)
             dbe.commit()
             dbe.close()
             return ActionDisplayAllUser(request)
        except Exception as e:
            print(e)
            return ActionDisplayAllUser(request)

def ActionLogout(request):
    auth.logout(request)
    return render(request,"AdminLogin.html",{'msg':""})
