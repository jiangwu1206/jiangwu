#!/usr/bin/python
# -*- coding: UTF-8 -*-

from selenium import webdriver
from fake_useragent import UserAgent
import time
import random
import json
import sys


#获取程序所在目录
dir=sys.path[0]

#定义浏览器参数
def browser():
    o=webdriver.ChromeOptions()
    ua=UserAgent()
    UA=ua.random
    o.add_argument('--user-agent='+UA)
    print(UA)
    o.add_argument('disable-infobars')
    o.add_argument('--headless')
    o.add_argument('--disable-gpu')
    o.add_argument('--window-size=1920,1080')
    o.add_argument('--proxy-server=SOCKS5://127.0.0.1:1080')
    o.add_argument('log-level=3')
    return webdriver.Chrome(options=o)


#判断IP是否重复
def IsReIP(b,IP):
    b.get("http://ip.cip.cc")
    ip=b.find_element_by_tag_name("body").text
    print(ip)
    if ip in IP:
        print("IP重复使用")
        q=input("请更换IP")    
        if 'q' == q:
            b.quit()
            exit(0)
        return IsReIP(b,IP)
    return ip
    
#读取配置文件并转换为字典
#读取配置文件并转换为字典
file=open(dir+'/config.py','r')
config=file.read()
file.close()
data=json.loads(config)
link=data["link"]


#当前累计点击次数
n=1

#已用IP变量
IP={}

while True:
    #广告名称
    name={}
    #定义点击次数;点击次数随机产生1至5之间
    cn=random.randint(1,5)
    WEB=browser()
    #判断IP是否重复
    ip=IsReIP(WEB,IP)
    IP[ip]={}
    for x in range(cn):
        #开始点击广告
        for ad in data["ad"]:
            print(data)
            try:
                WEB.get(link)
                div=WEB.find_element_by_id(data["ad"][ad])
                WEB.switch_to_frame(div.find_element_by_tag_name("iframe"))
                text=WEB.find_element_by_tag_name('a').text
                #当n为5不进行点击 模拟用户打开页面而不点击广告
                if n==5:
                    break
                print(text)
                #判断是否已经点过该条广告
                if text in name:
                    print("广告重复")
                    continue
                name[text]=""
                WEB.find_element_by_tag_name('a').click()

                #模拟人工滚动阅读
                '''
                for j in range(random.randint(1,3)):
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
    q=input("请更换IP")
    if 'q'==q:
        break


exit(0)