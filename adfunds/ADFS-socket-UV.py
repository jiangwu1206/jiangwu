#!/usr/bin/python
# -*- coding: UTF-8 -*-

from selenium import webdriver
from fake_useragent import UserAgent
from resolution import resolution
from bash import *
import time
import random
import json
import sys
import requests


#读取配置文件并转换为字典
data=config()
link=data["link"]

#已用IP变量
IP={}
#浏览次数
n=1
while True:
    try:
        #判断IP是否重复,并返回可用IP
        proxyip=socketIsReIP(IP)
    except:
        continue    
    try:
        #第一个参数为代理IP，第二个参数为是否启用代理1为启用
        WEB=browser(proxyip,1)
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
        WEB.quit()
        continue
        
    WEB.quit()
    if n==50 :
        exit(0)
    #time.sleep(random.randint(60,6000))
exit(0)