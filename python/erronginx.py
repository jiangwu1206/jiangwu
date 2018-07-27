# -*- coding: UTF-8 -*-
#!/bin/python/env
import time
import requests



'''
果酱
nginx 错误日志采集

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
        s=line
        statusCode=int(s[s.index('HTTP/1.1'):s.index('HTTP/1.1')+13][-3:])
        if 405 > statusCode :
            continue

        l=line.split()
        ulink=l[6].split('?')[0].split('/')
        try:
            data["url"]=ulink[1]+"/"+ulink[2]
        except:
            data["url"]=ulink[1]
        data["type"]=1
        data["content"]=statusCode
        data["ip"]=l[-1]
        data["client_ip"]=l[0]
        r=requests.get(url,params=data)
        print(r.url)
