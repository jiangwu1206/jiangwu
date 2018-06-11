import scrapy
import json
import time

class admin(scrapy.spiders.Spider):
    name = "test1"  # 爬虫的名字，执行时使用
    allowed_domains = ["admin.renqitv.cn"]  # 允许爬取的域名，非此域名的网页不会爬取
    start_urls = [
        "https://admin.renqitv.cn/user/login"
    ]

    def parse(self, response):  # 真正的爬虫方法
        data={'username':'tenfey','password':'tenfey2017@677'}
        print('开始登陆')
        yield scrapy.FormRequest(url='https://admin.renqitv.cn/user/checkPassword',formdata=data,callback=self.isLogin)
        print('数据已返回')


    def isLogin(self,response):
        b=json.loads(response.body)
        print(b)
        if 0 == b['errno'] :
            print('登陆成功')
            data = {
                'status':'0',
               'page': '1',
               'rows': '10'
            }
            while (True):
                yield scrapy.FormRequest(url='https://admin.renqitv.cn/userInfo/userfeedback',formdata=data, callback=self.Customer,dont_filter = True)


    def Customer(self,response):
        print("数据已返回")
        b=json.loads(response.body)
        print("==============================================================================================================================================")
        for i in b['rows']:
            print("用户ID\t信息类型\t状态\t\t反馈时间\t设备ID\t\t订单号")
            print(i['uid']+"\t",i['type']+"\t",i['status']+"\t",i['add_time']+"\t",i['device_id']+"\t",i['order_no'])
            print("信息内容",i['content'])
            print("\n")

        time.sleep(10)

