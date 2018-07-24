#!/usr/bin/python
# -*- coding: UTF-8 -*-

from selenium import webdriver
import time
import random
import json


#定义浏览器参数
o=webdriver.ChromeOptions()
o.add_argument('--user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"')
o.add_argument('disable-infobars')
#o.add_argument('--headless')
o.add_argument('--disable-gpu')
o.add_argument('--window-size=1024,768')
o.add_argument('log-level=3')

#读取配置文件并转换为字典
file=open('config.py','r')
config=file.read()
file.close()
data=json.loads(config)
link=data["link"]

n=1

#定义浏览器变量
b={}
for ad in data["ad"]:
    b[ad]={}

while True:
    print(n)
    n+=1
#    if n==200:
#        break
    
    #启动浏览器点击广告
    #定义点击次数;点击次数随机产生1至3之间
    cn=random.randint(1,3)
    for x in range(cn):
        b[x]=webdriver.Chrome(options=o)
        for ad in b:
            try:
                b[x].get(link)
                div=b[x].find_element_by_id(data['ad'][ad])
                b[x].switch_to_frame(div.find_element_by_tag_name("iframe"))
                b[x].find_element_by_tag_name('a').click()
                #print(data['ad'][ad])
                #模拟人工滚动阅读
                for j in range(random.randint(3,6)):
                    js="var q=document.documentElement.scrollTop="+str(random.randint(300,10000))
                    b[x].execute_script(js)
                    time.sleep(random.randint(2,5))
                
            except:
                continue
        
        '''
        #关闭浏览器    
        for ad in b:
            try:
                b[ad][x].quit()
            except:
                continue
                
        '''        
    for x in range(cn):
        try:
            b[x].quit()
        except:
            continue
#    break

exit(0)