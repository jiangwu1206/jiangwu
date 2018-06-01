import os


"""

interface eth0
static ip_address=192.168.0.2/16
static routers=192.168.0.1
static domain_name_servers=223.5.5.5 223.6.6.6

"""

print("请输入主机号")
host_num=input()
host_num=int(host_num)
s_ip="192.168.0.2/16"

while(True):
	if(255 > host_num):
		with open("f:/ip","r+") as f:
			
			ip=f.read()			
			d_ip="192.168.0."+str(host_num)+"/16"
			f.seek(0)
			f.write(ip.replace(s_ip,d_ip))
			host_num=host_num+1
			print(d_ip)
			os.system("pause")
