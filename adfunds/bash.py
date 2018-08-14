#!/usr/bin/python
# -*- coding: UTF-8 -*-

from selenium import webdriver
from checkport import IsOpen
from fake_useragent import UserAgent
from resolution import resolution
import json
import sys
import requests


#定义浏览器参数
def browser(proxyip=None,proxy=None):
    o=webdriver.ChromeOptions()
    ua=UserAgent()
    UA=ua.random
    o.add_argument('--user-agent=%s'%(UA))
    #print(UA)
    o.add_argument('disable-infobars')
    o.add_argument('--headless')
    o.add_argument('--disable-gpu')
    px=resolution().random()
    print(px)
    o.add_argument('--window-size=%s'%(px))
    if proxy==1:
        o.add_argument('--proxy-server=SOCKS5://%s:1080'%(proxyip))
    o.add_argument('log-level=3')
    return webdriver.Chrome(options=o)


#判断IP是否重复并记录-代理精灵版本
def dlIsReIP(IP,dl):
    ip=requests.get('http://ip.tenfey.com').text.strip()
    print(ip)
    print('本地内中存判断')
    if ip in IP:
        print("IP重复使用正在自动更换IP")
        dl.disconnect()
        dl.connect()
        return dlIsReIP(IP,dl)
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
            return dlIsReIP(IP,dl)
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

#判断IP是否重复并记录-socket5版本
def socketIsReIP(IP):
    try:
        #获取代理IP由服务器随机返回一个
        print('开始获取代理IP')
        proxyip=requests.get('http://127.0.0.1:8080/getip/').text.strip()
        if IsOpen(proxyip,1080):
            print('开始验证代理IP:%s'%(proxyip))
            ip=requests.get('http://ip.tenfey.com',proxies={'http': 'socks5://%s:1080'%(proxyip), 'https': 'socks5://%s:1080'%(proxyip)},timeout=10).text.strip()
        else:
            print('获取的代理IP:%s不可用,正在更换'%(proxyip))
            return socketIsReIP(IP)
    except:
        print('连接代理IP:%s超时,正在更换'%(proxyip))
        return socketIsReIP(IP)
    print(ip)
    print('本地内中存判断')
    if ip in IP:
        print("IP重复使用正在自动更换IP")
        return socketIsReIP(IP)
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
            return socketIsReIP(IP)
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
