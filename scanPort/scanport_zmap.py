from checkport import IsOpen
import time
import threading
import pymysql
import requests
import IPy
from concurrent.futures import ProcessPoolExecutor
import subprocess

'''

ZMAP用于扫描结合python 进行验证

'''
 

def check(ip,port):
    if IsOpen(ip,port):
        try:
            if requests.head('http://47.104.141.156:180',timeout=1,proxies={'http':'socks5://%s:1080'%(ip),'https':'socks5://%s:1080'%(ip)}).ok :
                print('有效IP:%s'%(ip))
            else:
                return 0
        except:
            return 0
            
        try:
            # 打开数据库连接
            db = pymysql.connect("10.0.6.39","test","test","test")
        except:
            print('数据库连接失败')
            del port
            del ip
            del db
            return 0
        
        try:     
            # 使用 cursor() 方法创建一个游标对象 cursor
            cursor = db.cursor()
            # 使用 execute()  方法执行 SQL 查询 
            cursor.execute('INSERT INTO t VALUES(%s)',(ip))
            db.commit()
            # 关闭数据库连接
            db.close()
            del port
            del ip
            del db
            return 0
        except:
            print('发生异常插入失败')
            db.close()
            del port
            del ip
            del db
            return 0

        
if __name__=='__main__':
    print(time.time())
    p=subprocess.Popen('zmap -w cn.txt -p 1080 -o 1080.txt -B 5M')
    time.sleep(2)
    file=open('1080.txt','r')
    port='1080'
    while True:
        where=file.tell()
        text=file.readline()
        ip=text.strip()
        if not ip:
            time.sleep(0.5)
            file.seek(where)
            del where
            del ip
            #判断zmap是否结束
            if not p.poll():
                return 0
            continue
        else:
            check(ip,port)
            del where,ip,text
    file.close()
    del file
    del port