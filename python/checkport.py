#!/usr/bin/python
# -*- coding: UTF-8 -*-

import socket


'''

检测目标IP是否开放指定端口

'''

def IsOpen(host,port):
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.settimeout(3)
    try:
        port=int(port)
        s.connect((host,port))
        s.shutdown(2)       
        print("ip:%s port:%d is open" %(host,port))
        return True
    except:
        print("ip:%s port:%d is down" %(host,port))
        return False
