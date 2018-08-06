from django.shortcuts import render
from django.http import HttpResponse
import pymysql


# Create your views here.


#插入当前使用的IP
def insert(request):
    if request.method == 'POST':
        try:
            # 打开数据库连接
            db = pymysql.connect("10.0.6.39","test","test","test")
        except:
            return HttpResponse('连接数据库异常')
        
        try:     
            #获取请求参数
            ip=request.POST['ip'].strip()
            sql='INSERT INTO ip VALUES("'+ip+'")'
            print(sql)
            # 使用 cursor() 方法创建一个游标对象 cursor
            cursor = db.cursor()
             
            # 使用 execute()  方法执行 SQL 查询 
            if(cursor.execute(sql)):
                db.commit()
                return HttpResponse('True')
            else:
                return HttpResponse('False')

             
            # 关闭数据库连接
            db.close()
            
        except:
            return HttpResponse('发生异常插入失败')
            db.close()
    else:
        return HttpResponse()
        
#查询IP是否使用过
def query(request):
    if request.method == 'POST':
        try:
            # 打开数据库连接
            db = pymysql.connect("10.0.6.39","test","test","test")
        except:
            return HttpResponse('连接数据库异常')
        
        try:
            #获取请求参数
            ip=request.POST['ip'].strip()
            print(ip)
            #存在SQL注入风险
            sql='SELECT * FROM ip WHERE ip="'+ip+'"'
            print(sql)
            # 使用 cursor() 方法创建一个游标对象 cursor
            cursor = db.cursor()
             
            # 使用 execute()  方法执行 SQL 查询 
            if(cursor.execute(sql)):
                return HttpResponse('True')
            else:
                return HttpResponse('False')

             
            # 关闭数据库连接
            db.close()
        except:
            return HttpResponse('发生异常查询失败')
            db.close()
    else:
        return HttpResponse()