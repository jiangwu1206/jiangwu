#!/usr/bin/python
# -*- coding: UTF-8 -*-

from selenium import webdriver
from fake_useragent import UserAgent
from resolution import resolution
from dlip import ipjl
from bash import *
import time
import random
import json
import sys
import requests




'''

IP精灵版本
IP精灵需加入环境变量中

'''


#打开IP精灵
dl=ipjl()
dl.open()


#读取配置文件并转换为字典
data=config()
link=data["link"]



#已用IP变量
IP={}

#浏览次数
n=1

while True:
    #使用IP精灵
    dl.connect()
    
    try:
        WEB=browser()
        #判断IP是否重复
        ip=dlIsReIP(WEB,IP,dl)
    except:
        WEB.quit()
        continue    
    try:
        WEB.get(link)
        '''
        #模拟页面滚动浏览
        for j in range(random.randint(1,5)):
                js="var q=document.documentElement.scrollTop="+str(random.randint(300,10000))
                WEB.execute_script(js)
                time.sleep(random.randint(2,5))
        '''   
        print(n)
        n+=1
    except:
        print("发生异常")
        continue
        
    WEB.quit()
    dl.disconnect()
    if n==50 :
        exit(0)
    time.sleep(random.randint(60,6000))

dl.logout()
exit(0)