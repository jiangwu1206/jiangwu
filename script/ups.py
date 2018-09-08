#!/usr/bin/pyenv
#coding:utf-8

import os
import time

for x in range(5):
    ret=os.system('ping -c 3 192.168.31.1')
    if(0 != ret):
        if(3<x):
            os.system("/usr/sbin/systemctl stop mysqld")
            os.system("/usr/sbin/systemctl stop redis")
            os.system("/usr/bin/supervisorctl stop all")
            time.sleep(5)
            os.system("/usr/sbin/shutdown -P now")
        continue
    break