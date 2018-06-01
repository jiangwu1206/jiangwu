import os

a=0

with open("/root/20171218list.log","r") as f:
	for line in f:
		cp=line
		#cp=cp+" /root/log/"
		os.system(cp)
		if(35000==a):
			break
		a=a+1
		print(a)
		print(cp)