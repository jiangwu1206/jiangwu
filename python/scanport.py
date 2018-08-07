from checkport import IsOpen
import time
import threading
import pymysql


#test
#14:50 start scan

def check(ip,port):
    if IsOpen(ip,port):
        try:
            # 打开数据库连接
            db = pymysql.connect("10.0.6.39","test","test","test")
        except:
            print('数据库连接失败')
        
        try:     
            # 使用 cursor() 方法创建一个游标对象 cursor
            cursor = db.cursor()
            # 使用 execute()  方法执行 SQL 查询 
            cursor.execute('INSERT INTO proxy VALUES(%s)',(ip))
            db.commit()
            # 关闭数据库连接
            db.close()
            
        except:
            print('发生异常插入失败')
            db.close()

def scan():
    global ip1,ip2,ip3,ip4,port
    while True:
        if ip4>255:
            ip4=0
            ip3+=1
        if ip3>255:
            ip3=0
            ip2+=1
        if ip2>255:
            ip2=0
            ip1+=1
            
        #避开局域网IP
        if ip1==10:
            ip1+=1
        if ip1==192 and ip2==168:
            ip2+=1
        if ip1==172 and ip2>15 and ip2<32:
            ip2=32
        if ip1>255:
            print('已扫描全网')
            break
        
        ip=str(ip1)+"."+str(ip2)+"."+str(ip3)+"."+str(ip4)
        ip4+=1
        threading.Thread(target=check,args=(ip,port)).start()


ip1,ip2,ip3,ip4=1,0,0,1
port=1080
ip=''        
if __name__=='__main__':
    scan()
    