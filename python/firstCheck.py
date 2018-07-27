#!/usr/bin/python
# -*- coding: UTF-8 -*-

from checkport import IsOpen
from pymongo import MongoClient

'''

初步验证代理是否可用
判断依据为是否开放指定端口

'''


conn=MongoClient("10.0.6.211",27017)
db=conn.proxyip
my_set=db.t1
new_set=db.t2

for x in my_set.find():
    p={}
    if IsOpen(x["ip"],x["port"]):
        p["ip"]=x["ip"]
        p["port"]=x["port"]
        p["type"]=x["type"]
        new_set.insert_one(p)

conn.close()