#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
import smtplib
from email.mime.text import MIMEText
from email.header import Header
 
# 第三方 SMTP 服务
mail_host="smtp.ym.163.com"  #设置服务器
mail_user="alert@tenfey.com"    #用户名
mail_pass="alert110"   #口令 
 
 
sender = 'alert@tenfey.com'
receivers = ['tenfey@guojiang.tv','1073943388@qq.com','haifeng@guojiang.tv','dante@guojiang.tv']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
 
message = MIMEText('请求发生50x告警；请登陆日志系统查看相关信息http://117.50.16.122', 'plain', 'utf-8')
message['From'] = Header("alert@tenfey.com", 'utf-8')
message['To'] =  Header("haifeng@guojiang.tv", 'utf-8')
 
subject = '请求发生50x告警'
message['Subject'] = Header(subject, 'utf-8')
 
 
try:
    smtpObj = smtplib.SMTP(mail_host, 25)
    #smtpObj = smtplib.SMTP_SSL(mail_host, 465) #TLS方式
    smtpObj.login(mail_user,mail_pass)  
    smtpObj.sendmail(sender, receivers, message.as_string())
    print ("邮件发送成功")
except smtplib.SMTPException:
    print ("Error: 无法发送邮件")
