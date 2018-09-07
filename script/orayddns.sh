#!/bin/bash
domain="domain"
user="user"
pwd="pwd"
ip=`curl -s ip.tenfey.com`
oldip=`host jw1206.xicp.net |awk '{print $NF}'`
if [ "$ip"x != "$oldip"x ];then
echo '不等'
/usr/bin/curl "http://$user:$pwd@ddns.oray.com/ph/update?hostname=$domain"
fi

echo $ip
echo $oldip
