#! /usr/bin/env python
# coding=utf-8

import random
import string
import os
import json


'''

随机批量添加邮箱账号；该脚本可用于批量添加系统用户

'''


#用户字典
userDict={}

#随机创建100个用户并设定密码,如果用户名生成出现重复则不创建用户
for i in range(100):
    user = ''.join(random.sample(string.ascii_letters + string.digits, random.randint(3,8)))
    endPass = ''.join(random.sample(string.ascii_letters + string.digits, random.randint(1,3)))
    if user in userDict:
        continue
    userDict[user]=user+endPass
    #创建用户并禁止用户登录系统终端
    os.system('useradd -m %s -g mail -s /bin/false' % user)
    #设定用户密码
    os.system('echo %(pass)s |passwd --stdin %(name)s' % {'name':user,'pass':userDict[user]})
    
#将用户名密码保存到文件
f=open('mailUserInfo.txt','w+')
jsObj=json.dumps(userDict)
f.write(jsObj)
f.close()

#打印出用户名与密码
print(userDict)

