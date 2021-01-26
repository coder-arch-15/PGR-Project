from django.shortcuts import render
import pymysql as mysql
from django.views.decorators.clickjacking import xframe_options_exempt

def ActionUserInterface(request):
        return render(request,"userregister.html",{"msg":''})

def ActionUserSubmit(request):
      try:
        name = request.POST["nickname-25"]
        username=request.POST["user_login-25"]
        email = request.POST["user_email-25"]
        mob = request.POST["mobile_number-25"]
        password = request.POST["user_password-25"]
        dbe=mysql.connect(host='localhost',port=3306,password='123',user='root',db='dummy')
        cmd=dbe.cursor()
        q="insert into user(cname,username,email,mob,pasw) values('{0}','{1}','{2}','{3}','{4}')".format(name,username,email,mob,password)
        cmd.execute(q)
        dbe.commit()
        dbe.close()
        return render(request,"userregister.html",{"msg":"record submitted"})

      except Exception as e:
        print(e)
        return render(request, "userregister.html", {"msg": "record not submitted"})


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