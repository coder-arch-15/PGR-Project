from django.shortcuts import render
import pymysql as mysql
from django.views.decorators.clickjacking import xframe_options_exempt

def ActionUserInterface(request):
        return render(request,"UserInterface.html",{"msg":''})

def ActionUserSubmit(request):
      try:
        cname = request.POST['cname']
        contact=request.POST['contact']
        gender=request.POST['gender']
        userid = request.POST['userid']
        password = request.POST['password']
        dbe=mysql.connect(host='localhost',port=3306,password='123',user='root',db='dummy')
        cmd=dbe.cursor()
        q="insert into user(username,contact,gender,userid,password) values('{0}','{1}','{2}','{3}','{4}')".format(cname,contact,gender,userid,password)
        cmd.execute(q)
        dbe.commit()
        dbe.close()
        return render(request,"UserInterface.html",{"msg":"record submitted"})

      except Exception as e:
        print(e)
        return render(request, "UserInterface.html", {"msg": "record not submitted"})


def ActionDisplayAllUser(request):
    try:

     dbe = mysql.connect(host='localhost', port=3306, password='123', user='root', db='dummy')
     cmd = dbe.cursor()
     q = "select U.* from user U"
     cmd.execute(q)
     rows=cmd.fetchall()
     dbe.close()
     return render(request,"UserDisplayAll.html",{"rows":rows})
    except Exception as e:
        print(e)
        return render(request, "UserDisplayAll.html", {"rows":[]})


def ActionDisplayById(request):
    try:
     ccid=request.GET['ccid']
     dbe = mysql.connect(host='localhost', port=3306, password='123', user='root', db='dummy')
     cmd = dbe.cursor()
     q = "select * from user where id={0}".format(ccid)
     cmd.execute(q)
     row=cmd.fetchone()
     dbe.close()
     return render(request,"UserDisplayById.html",{"row":row})
    except Exception as e:
        print(e)
        return render(request, "UserDisplayById.html", {"row":[]})


def ActionUserEditDeleteSubmit(request):
        ccid=request.POST['ccid']
        btn=request.POST['btn']
        try:
         if(btn=='Pending'):
          dbe=mysql.connect(host='localhost',port=3306,password='123',user='root',db='dummy')
          cmd=dbe.cursor()
          q="update user set adminact='{0}' where id={1}".format(btn,ccid)
          cmd.execute(q)
          dbe.commit()
          dbe.close()
          return ActionDisplayAllUser(request)
         elif(btn=='Approved'):
             dbe = mysql.connect(host='localhost', port=3306, password='123', user='root', db='dummy')
             cmd = dbe.cursor()
             q = "update user set adminact='{0}' where id={1}".format(btn, ccid)
             cmd.execute(q)
             dbe.commit()
             dbe.close()
             return ActionDisplayAllUser(request)
         elif (btn == 'DisApproved'):
             dbe = mysql.connect(host='localhost', port=3306, password='123', user='root', db='dummy')
             cmd = dbe.cursor()
             q = "update user set adminact='{0}' where id={1}".format(btn, ccid)
             cmd.execute(q)
             dbe.commit()
             dbe.close()
             return ActionDisplayAllUser(request)
        except Exception as e:
            print(e)
            return ActionDisplayAllUser(request)

@xframe_options_exempt
def ActionDisplayAllUserLogin(request):
    try:

     dbe = mysql.connect(host='localhost', port=3306, password='123', user='root', db='dummy')
     cmd = dbe.cursor()
     q = "select * from user"
     cmd.execute(q)
     rows=cmd.fetchall()
     dbe.close()
     return render(request,"UserDisplayAllLogin.html",{"rows":rows})
    except Exception as e:
        print(e)
        return render(request, "UserDisplayAllLogin.html", {"rows":[]})

@xframe_options_exempt
def ActionDisplayByIdLogin(request):
    try:
     ccid=request.GET['ccid']
     dbe = mysql.connect(host='localhost', port=3306, password='123', user='root', db='dummy')
     cmd = dbe.cursor()
     q = "select * from user where id={0}".format(ccid)
     cmd.execute(q)
     row=cmd.fetchone()
     dbe.close()
     return render(request,"UserDisplayByIdLogin.html",{"row":row})
    except Exception as e:
        print(e)
        return render(request, "UserDisplayByIdLogin.html", {"row":[]})



@xframe_options_exempt
def ActionUserEditDeleteSubmitLogin(request):
    ccid = request.POST['ccid']
    cname = request.POST['cname']
    contact = request.POST['contact']
    gender = request.POST['gender']
    userid = request.POST['userid']
    password = request.POST['password']
    btn = request.POST['btn']
    try:
        if (btn == 'Edit'):
            dbe = mysql.connect(host='localhost', port=3306, password='123', user='root', db='dummy')
            cmd = dbe.cursor()
            q = "update user set username='{0}',contact='{1}',gender='{2}',userid='{3}',password='{4}' where id={5}".format(
                cname,contact,gender,userid,password,ccid)
            cmd.execute(q)
            dbe.commit()
            dbe.close()
            return ActionDisplayAllUserLogin(request)
        elif (btn == 'Delete'):
            dbe = mysql.connect(host='localhost', port=3306, password='123', user='root', db='dummy')
            cmd = dbe.cursor()
            q = "delete from user where id={0}".format(ccid)
            cmd.execute(q)
            dbe.commit()
            dbe.close()
            return ActionDisplayAllUserLogin(request)
    except Exception as e:
        print(e)
        return ActionDisplayAllUserLogin(request)