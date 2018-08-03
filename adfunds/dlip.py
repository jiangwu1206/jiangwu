import os
import time
import requests
from bs4 import BeautifulSoup

class ipjl:
    #打IP精灵并登陆
    def open(self):
        os.popen("ipjl.exe -user=ldt195175108 -pwd=537719299@ -force -page=0")
        time.sleep(20)
    
    #动作执行
    def __exec(self,url,key,value):
        r=requests.get(url)
        bs=BeautifulSoup(r.text,'lxml')
        code=int(bs.find(key).text)
        if value==code:
            return True
        else:
            return False

    #退出IP精灵
    def logout(self):
        try:
            url="http://127.0.0.1:8222/logout/"
            value=0
            key="code"
            if self.__exec(url,key,value):
                print("退出成功")
        except:
            print("IP精灵异常,请检查IP精灵是否已运行")

    #查看连接状态
    def info(self):
        try:
            url="http://127.0.0.1:8222/getstate/"
            value=11
            key="state"
            if self.__exec(url,key,value):
                print("当前状态已连接")
                return True
            else:
                print("当前状态未连接")
                return False
        except:
            print("IP精灵异常,请检查IP精灵是否已运行")
    
    #断开连接
    def disconnect(self):
        try:
            url="http://127.0.0.1:8222/disconnect/"
            key="code"
            value=0
            self.__exec(url,key,value)
            time.sleep(5)
            if not self.info():
                print("断开连接成功")
                return True
            else:
                print("连接断开失败,请检查是否有建立连接")
                return False
        except:
            print("IP精灵异常,请检查IP精灵是否已运行")
            
    #随机连接某一条静态线路
    def connect(self):
        try:
            url="http://127.0.0.1:8222/stconnect/"
            key="code"
            value=0
            self.__exec(url,key,value)
            time.sleep(5)
            if self.info():
                print("连接成功")
                return True
            else:
                print("连接断开失败,请检查之前是否有建立连接")
                return False
        except:
            print("IP精灵异常,请检查IP精灵是否已运行")
        



            
if __name__=='__main__':
    t=ipjl()
    t.open()
    input("继续")
    t.connect()
    input("继续")
    t.disconnect()
    input("继续")
    t.logout()
    