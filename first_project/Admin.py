from django.shortcuts import render
from django.views.decorators.clickjacking import xframe_options_exempt
import pymysql as mysql



def ActionDisplayAllUser(request):
    try:
     dbe = mysql.connect(host='localhost', port=3306, password='123', user='root', db='dummy')
     cmd = dbe.cursor()
     q = "select D.* from dummy D where D.action=''"
     cmd.execute(q)
     rows=cmd.fetchall()
     dbe.close()
     return render(request,"UserDisplayAll.html",{"rows":rows})
    except Exception as e:
        print(e)
        return render(request, "UserDisplayAll.html", {"rows":[]})

@xframe_options_exempt
def ActionDisplayById(request):
  try:
    rec = request.session['ADMIN_SES']
    try:
     ccid=request.GET['ccid']
     dbe = mysql.connect(host='localhost', port=3306, password='123', user='root', db='minor')
     cmd = dbe.cursor()
     q = "select * from coordinator where coordinatorid={0}".format(ccid)
     cmd.execute(q)
     row=cmd.fetchone()
     dbe.close()
     return render(request,"CoordinatorDisplayById.html",{"row":row,"rec":rec})
    except Exception as e:
        print(e)
        return render(request, "CoordinatorDisplayById.html", {"row":[]})
  except:
      return render(request, "NewAdminLogin.html", {"msg": ''})
@xframe_options_exempt
def ActionCoordinatorEditDeleteSubmit(request):
        ccid=request.POST['ccid']
        name=request.POST['ename']
        cname = request.POST['cname']
        contact=request.POST['contact']
        btn=request.POST['btn']
        try:
         if(btn=='Edit'):
          dbe=mysql.connect(host='localhost',port=3306,password='123',user='root',db='minor')
          cmd=dbe.cursor()
          q="update coordinator set clubname='{0}',coordinatorname='{1}',contact='{2}' where coordinatorid={3}".format(name,cname,contact,ccid)
          cmd.execute(q)
          dbe.commit()
          dbe.close()
          return ActionDisplayAllCoordinator(request)
         elif(btn=='Delete'):
            dbe = mysql.connect(host='localhost', port=3306, password='123', user='root', db='minor')
            cmd = dbe.cursor()
            q = "delete from coordinator where coordinatorid={0}".format(ccid)
            cmd.execute(q)
            dbe.commit()
            dbe.close()
            return ActionDisplayAllCoordinator(request)
        except Exception as e:
            print(e)
            return ActionDisplayAllCoordinator(request)

@xframe_options_exempt
def ActionEditCoordinatorPicture(request):

    try:
        ccid = request.POST['ccid']
        file=request.FILES['eicon']
        dbe=mysql.connect(host='localhost',port=3306,password='123',user='root',db='minor')
        cmd=dbe.cursor()
        q="update coordinator set coordinatorpic='{0}' where ccid={1}".format(file.name,ccid)
        cmd.execute(q)
        dbe.commit()
        dbe.close()
        f=open("E:/minor/asset/"+file.name,"wb")
        for chunk in file.chunks():
            f.write(chunk)
        f.close()
        return ActionDisplayAllCoordinator(request)
    except Exception as e:
        print(e)
        return ActionDisplayAllCoordinator(request)