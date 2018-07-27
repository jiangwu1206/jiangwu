#! /usr/bin/env python
# coding=utf-8

import json
import os


'''
批量删除用户
'''

f=open('mailUserInfo.txt','r')
jsObj=f.read()
f.close()
userDict=json.loads(jsObj)
for key in userDict.keys():
    os.system('userdel -r %s' % key)
    print("%s 已删除" % key)