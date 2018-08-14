from django.shortcuts import render
from django.http import HttpResponse
import pymysql
import random


# Create your views here.


#插入当前使用的IP
def insert(request):
    if request.method == 'POST':
        try:
            # 打开数据库连接
            db = pymysql.connect("127.0.0.1","ip","adf123","iplist")
        except:
            return HttpResponse('连接数据库异常')
        
        try:     
            #获取请求参数
            ip=request.POST['ip'].strip()
            # 使用 cursor() 方法创建一个游标对象 cursor
            cursor = db.cursor()
            # 使用 execute()  方法执行 SQL 查询 
            if(cursor.execute('INSERT INTO ip VALUES(%s)',(ip))):
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
            db = pymysql.connect("127.0.0.1","ip","adf123","iplist")
        except:
            return HttpResponse('连接数据库异常')
        
        try:
            #获取请求参数
            ip=request.POST['ip'].strip()
            # 使用 cursor() 方法创建一个游标对象 cursor
            cursor = db.cursor()
            # 使用 execute()  方法执行 SQL 查询 
            if(cursor.execute('SELECT * FROM ip WHERE ip=%s',(ip))):
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

#从数据库数据提取一个IP
def getip(request):
    try:
        # 打开数据库连接
        db = pymysql.connect("127.0.0.1","ip","adf123","iplist")
    except:
        return HttpResponse('连接数据库异常')
    
    try:
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()
        # 使用 execute()  方法执行 SQL 查询
        cursor.execute('SELECT COUNT(*) FROM proxy')
        #获取列表总数
        count=cursor.fetchone()
        #随机获取一个IP
        num=random.randint(1,count[0])
        print(num)
        if(cursor.execute('SELECT * FROM proxy LIMIT %s,1',(num))):
            ip=cursor.fetchone()
            return HttpResponse('%s'%(ip[0]))
        else:
            return HttpResponse('False')

         
        # 关闭数据库连接
        db.close()
    except:
        return HttpResponse('发生异常查询失败')
        db.close()