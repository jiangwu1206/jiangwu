# -*- coding: UTF-8 -*-

from selenium import webdriver
import time
import random
import json


#定义浏览器参数
o=webdriver.ChromeOptions()
o.add_argument('--user-agent="Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.90 Safari/537.36 2345Explorer/9.4.1.17471"')
o.add_argument('disable-infobars')
o.add_argument('--headless')
o.add_argument('--disable-gpu')
o.add_argument('--window-size=1920,1080')

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
    
    
    #启动浏览器点击广告
    for ad in b:
        #定义点击次数;点击次数随机产生5至15之间
        cn=random.randint(5,15)
        for x in range(cn):
            try:
                b[ad][x]=webdriver.Chrome(options=o)
                b[ad][x].get(link)
                b[ad][x].find_element_by_id(data['ad'][ad]).click()        
            except:
                continue
        
        #关闭浏览器    
        for x in range(cn):
            try:
                b[ad][x].quit()
            except:
                continue

#    break

exit(0)
    
    