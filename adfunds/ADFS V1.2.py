#!/usr/bin/python
# -*- coding: UTF-8 -*-

from selenium import webdriver
from fake_useragent import UserAgent
import time
import random
import json




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
    o.add_argument('log-level=3')
    return webdriver.Chrome(options=o)



#读取配置文件并转换为字典
file=open('config.py','r')
config=file.read()
file.close()
data=json.loads(config)
link=data["link"]

#定义浏览器变量
b={}

for ad in data["ad"]:
    b[ad]={}

while True:  
    
    for ad in b:
        try:
            b[ad]=browser()
            b[ad].get(link)
            div=b[ad].find_element_by_id(data['ad'][ad])
            b[ad].switch_to_frame(div.find_element_by_tag_name("iframe"))
            b[ad].find_element_by_tag_name('a').click()
            #模拟人工滚动阅读
            for j in range(random.randint(3,5)):
                js="var q=document.documentElement.scrollTop="+str(random.randint(800,10000))
                b[ad].execute_script(js)
                time.sleep(random.randint(2,6))
        except:
            print("异常")
            continue
    
    #关闭浏览器    
    for ad in b:
        try:
            b[ad].quit()
        except:
            continue

    break

exit(0)