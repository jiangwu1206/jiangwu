num=int(input("请输入编号\n"))
endmaxnum=255
netnum=num//endmaxnum
basenetnum=1
lasthost=num%endmaxnum

if(netnum<basenetnum):
	netnum=basenetnum
else:
	netnum=netnum+basenetnum

if(lasthost == 0):
	lasthost=endmaxnum
	netnum=netnum-basenetnum

ip="192.168."+str(netnum)+"."+str(lasthost)
print(ip)