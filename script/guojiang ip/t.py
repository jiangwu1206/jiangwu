import os
"""
print("请输入替换前的内容")
s_ip=input()
print("请输入替换后的内容")
d_ip=input()
"""
with open("d:/flie.txt","r") as f:
	"""
	ip=f.read()
	f.seek(0)
	f.write(ip.replace(s_ip,d_ip))	
	"""
	for line in f:
		a=line+"123456"
		print(a)
		print("==========================")
		s=line.split('\n')
		print(s)
		print("++++++++++++++++")
		s=s[0]+"963"
		print(s)
		os.system("pause")