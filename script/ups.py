#!/usr/bin/pyenv
#coding:utf-8

import os
import time

for x in range(5):
    ret=os.system('ping -c 3 192.168.31.1')
    if(0 != ret):
        if(3<x):
            os.system("systemctl stop mysqld")
            os.system("systemctl stop redis")
            os.system("supervisorctl stop all")
            time.sleep(5)
            os.system("shutdown -P now")
        continue
    break