#!/usr/bin/python
# -*- coding: UTF-8 -*-

from selenium import webdriver
from fake_useragent import UserAgent
from resolution import resolution
import json
import sys
import requests


#定义浏览器参数
def browser():
    o=webdriver.ChromeOptions()
    ua=UserAgent()
    UA=ua.random
    o.add_argument('--user-agent=%s'%(UA))
    #print(UA)
    o.add_argument('disable-infobars')
    o.add_argument('--headless')
    o.add_argument('--disable-gpu')
    px=re.random()
    print(px)
    o.add_argument('--window-size=%s'%(px))
    #o.add_argument('--proxy-server=SOCKS5://127.0.0.1:1080')
    o.add_argument('log-level=3')
    return webdriver.Chrome(options=o)


#判断IP是否重复并记录
def IsReIP(b,IP):
    b.get("http://ip.tenfey.com")
    ip=b.find_element_by_tag_name("body").text
    print(ip)
    print('本地内中存判断')
    if ip in IP:
        print("IP重复使用正在自动更换IP")
        dl.disconnect()
        dl.connect()
        return IsReIP(b,IP)
    else:
        IP[ip]={}
    try:    
        print('远程数据库中判断')
        postdata={}
        postdata['ip']=ip.strip()
        #ipcheck为True时证明数据库中已存在该IP
        ipcheck=requests.post('http://ipcheck.tenfey.com/query/',data=postdata).text
        if 'True' == ipcheck:
            print("IP重复使用正在自动更换IP")
            dl.disconnect()
            dl.connect()
            return IsReIP(b,IP)
        elif 'False' == ipcheck:
            ipcheck=requests.post('http://ipcheck.tenfey.com/insert/',data=postdata).text
            if 'True' == ipcheck:
                pass
            elif 'False' == ipcheck:
                print('IP记录远程数据库失败')
            else:
                print(ipcheck)
        else:
            print(ipcheck)
    except:
        print('远程验证失败,请检查网络是否正常')

    return ip



    
#读取配置文件并转换为字典
def config():
    file=open('%s/config.py'%(sys.path[0]),'r')
    config=file.read()
    file.close()
    data=json.loads(config)
    return data
