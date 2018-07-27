# -*- coding: UTF-8 -*-
#!/bin/python/env
import time
import requests


'''
果酱

Nginx 请求响应超过指定时间日志采集

'''

file=open('/data/log/nginx/app.guojiang.tv.access.log','r')

file.seek(-1,2)

url="http://service.guojiang.tv/monitor/alarmUrl"
data={}

while True:
    where=file.tell()
    line=file.readline()
    if not line:
        time.sleep(0.5)
        file.seek(where)
        continue
    else:
        line=line.strip('\n')
        if '' == line:
            continue
        l=line.split()
        if 1 > float(l[-2]):
            continue
        ulink=l[6].split('?')[0].split('/')
        try:
            data["url"]=ulink[1]+"/"+ulink[2]
        except:
            data["url"]=ulink[1]
        data["type"]=2
        data["content"]=l[-2]
        data["ip"]=l[-1]
        data["client_ip"]=l[0]
        r=requests.get(url,params=data)
        print(r.url)
