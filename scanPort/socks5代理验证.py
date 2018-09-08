from checkport import IsOpen
import time
import requests
import IPy
import multiprocessing
import os
import threading

 
#检查目标IP是否可用
def check(ip,port=1080):
    print(ip)
    if IsOpen(ip,port):
        try:
            if requests.head('http://ip.tenfey.com',timeout=3,proxies={'http':'socks5://%s:1080'%(ip),'https':'socks5://%s:1080'%(ip)}).ok :
                print('===========有效socks5代理IP:%s=============='%(ip))
                postdata={}
                postdata['ip']=ip.strip()
                print(requests.post('http://ipcheck.tenfey.com/proxyipinsert/',data=postdata).text)
            else:
                return 0
        except:
            return 0


if __name__=='__main__':
    print(time.time())
    file=open('1080.txt','r')
    for ip in file:
        threading.Thread(target=check,args=(ip.strip(),)).start()
        time.sleep(0.0005)
    file.close()
    del file
    print(time.time())
    input("继续")