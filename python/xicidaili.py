#!/usr/bin/python
# -*- coding: UTF-8 -*-

from pymongo import MongoClient
from lxml import etree
import requests


'''

抓取西刺代理网站 免费代理IP存入Mongodb

'''




conn=MongoClient("10.0.6.211",27017)
db=conn.proxyip
my_set=db.t1

headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}
r=requests.get("http://www.xicidaili.com",headers=headers)

s=etree.HTML(r.text)
#提取IP和端口存入mongodb
for i in s.xpath('//*[@id="ip_list"]/tr'):
    d=i.xpath('.//td/text()')
    p={}
    try:
       p["ip"]=d[0]
       p["port"]=d[1]
       my_set.insert_one(p)
    except:
        continue

conn.close()