import requests
from bs4 import BeautifulSoup
import re

headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}

uri="http://www.kuaishouvideo.com/"
print("输入小写q表示退出")
while True:
    id=input("请输入主播ID:")
    if 'q'==id:
        exit(0)
    try:
        id=id.strip()
        int(id)
        url=uri+str(id)
    except:
        print("主播ID只能是数字")
        continue
    try:    
        r=requests.get(url,headers=headers)
    except:
        print("请检查网络连接是否正常")
        continue
    try:
        bs=BeautifulSoup(r.text,'html.parser')
        js=bs.body.findAll("script")[1]
        js =js.contents
        jstr=js[0]
        pyl=re.search('''(playUrl)(.*\w)''',jstr)
        pyl=pyl[0]
        pyl=pyl.split('":"')[1]
        pyl=pyl.replace('\\',"")
        print(pyl)
    except:
        print("该主播不存在")
        continue