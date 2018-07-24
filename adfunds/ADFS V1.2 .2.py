#!/usr/bin/python
# -*- coding: UTF-8 -*-

from selenium import webdriver
from fake_useragent import UserAgent
import time
import random
import json


#读取配置文件并转换为字典
file=open('config.py','r')
config=file.read()
file.close()
data=json.loads(config)
link=data["link"]

n=1

#定义浏览器变量
b={}

ua=UserAgent()
for ad in data["ad"]:
    b[ad]={}

while True:
    print(n)
    n+=1
#    if n==200:
#        break
    
    #启动浏览器点击广告
    for ad in b:
        #定义点击次数;点击次数随机产生1至3之间
        cn=random.randint(10,13)
        for x in range(cn):
            try:
            
                
                #定义浏览器参数
                o=webdriver.ChromeOptions()
                o.add_argument('--user-agent='+ua.random)
                o.add_argument('disable-infobars')
                o.add_argument('--headless')
                o.add_argument('--disable-gpu')
                o.add_argument('--window-size=1920,1080')
                o.add_argument('log-level=3')


                b[ad][x]=webdriver.Chrome(options=o)
                b[ad][x].get(link)
                div=b[ad][x].find_element_by_id(data['ad'][ad])
                b[ad][x].switch_to_frame(div.find_element_by_tag_name("iframe"))
                b[ad][x].find_element_by_tag_name('a').click()
                
                #模拟人工滚动阅读
                for j in range(random.randint(3,5)):
                    js="var q=document.documentElement.scrollTop="+str(random.randint(800,10000))
                    b[ad][x].execute_script(js)
                    time.sleep(random.randint(1,3))
                   
            #except:
            #    print("发生异常")
            #    continue
           
        
        #关闭浏览器    
        for x in range(cn):
            try:
                b[ad][x].quit()
            except:
                continue

#    break

exit(0)