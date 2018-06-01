#!/bin/bash

domain=jw1206.xicp.net
orayUser=jw1206
orayPassword=513029
oldIP=$(host jw1206.xicp.net |awk '{print $4}')
newIP=$(curl -s ifconfig.me)

if [ "$oldIP"x != "$newIP"x ]
then
	echo "不相等"
	curl http://$orayUser:$orayPassword@ddns.oray.com/ph/update?hostname=$domain&myip=$newIP
else
	echo 
fi