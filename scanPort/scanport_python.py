from checkport import IsOpen
import time
import requests
import IPy
import multiprocessing

 
#检查目标IP是否可用
def check(ip,port=1080):
    if IsOpen(ip,port):
        print(ip)
        try:
            if requests.head('http://ip.tenfey.com',timeout=3,proxies={'http':'socks5://%s:1080'%(ip),'https':'socks5://%s:1080'%(ip)}).ok :
                print('有效IP:%s'%(ip))
                postdata={}
                postdata['ip']=ip.strip()
                print(requests.post('http://ipcheck.tenfey.com/proxyipinsert/',data=postdata).text)
            else:
                return 0
        except:
            return 0

#迭代IP段
def forIPy(iprange):
    try:
        ipl=IPy.IP(iprange)
        for ip in ipl:
            check(str(ip).strip())

    except Exception as e:
        print("forIPy",e)

if __name__=='__main__':
    print(time.time())
    file=open('cn.txt','r')
    pool=multiprocessing.Pool()
    for iprange in file:
        pool.apply_async(forIPy,args=(iprange.strip(),))
    file.close()
    pool.close()
    pool.join()
    del file
    print(time.time())
    input("继续")