#!/usr/bin/env python
# -*- coding: utf-8 -*-

def dev_to_ip(dev_num):
	#设备编号
	num=dev_num

	#设定单网段最大主机号
	endmaxnum=255

	#计算网段号
	netnum=num//endmaxnum

	#设置开始网段号
	basenetnum=1

	#计算网络主机号
	lasthost=num%endmaxnum

	#对网段号进行偏移
	if(netnum<basenetnum):
		netnum=basenetnum
	else:
		netnum=netnum+basenetnum

	#对主机号进行偏移
	if(lasthost == 0):
		lasthost=endmaxnum
		netnum=netnum-1

	#拼接IP
	ip="192.168."+str(netnum)+"."+str(lasthost)
	return ip

if __name__ == "__main__":
	while True:
		num=input("请输入主机编号")
		if('q' == num):
			exit(0)
		print (dev_to_ip(int(num)))

