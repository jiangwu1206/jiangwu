#!/usr/bin/python
# -*- coding: UTF-8 -*-

from selenium import webdriver
from fake_useragent import UserAgent
from bash import *
from dlip import ipjl
import time
import random
import json
import sys




'''
IP精灵版本
IP精灵需加入环境变量中
'''


#打开IP精灵
dl=ipjl()
#dl.open()

#读取配置文件并转换为字典
data=config()
link=data["link"]


#当前累计点击次数
n=1

#已用IP变量
IP={}

while True:
    #使用IP精灵
    dl.connect()

    #定义外层for循环次数
    cn=2
    
    try:
        WEB=browser()
        #判断IP是否重复
        ip=dlIsReIP(WEB,IP,dl)
        IP[ip]={}
    except:
        WEB.quit()
        continue
    
    #range(2)表示 0到2 不包含2
    for x in range(cn):
        #开始点击广告
        for ad in data["ad"]:
            print(data)
            try:
                WEB.get(link)
                div=WEB.find_element_by_id(data["ad"][ad])
                WEB.switch_to_frame(div.find_element_by_tag_name("iframe"))
                text=WEB.find_element_by_tag_name('a').text
                #当n为1不进行点击 模拟用户打开页面而不点击广告
                if cn==1:
                    break
                print(text)
                WEB.find_element_by_tag_name('a').click()

                #模拟人工滚动阅读
                for j in range(random.randint(1,3)):
                    js="var q=document.documentElement.scrollTop="+str(random.randint(300,10000))
                    WEB.execute_script(js)
                    time.sleep(random.randint(2,5))
                print(n)
                n+=1
            except:
                print("发生异常")
                continue
        
    WEB.quit()
    dl.disconnect()
    q=input("请更换IP")
    if 'q'==q:
        break

dl.logout()
exit(0)