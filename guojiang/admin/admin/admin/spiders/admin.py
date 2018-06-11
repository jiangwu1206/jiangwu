import scrapy
import json
import time

class admin(scrapy.spiders.Spider):
    name = "admin"  # 爬虫的名字，执行时使用
    allowed_domains = ["admin.renqitv.cn"]  # 允许爬取的域名，非此域名的网页不会爬取
#    start_urls = [
#        "https://admin.renqitv.cn/user/login"
#    ]

    def start_requests(self):
         return [scrapy.Request('https://admin.renqitv.cn/user/login',meta={'cookiejar': 1},callback=self.parse)]


    def parse(self, response):  # 真正的爬虫方法
        data={'username':'tenfey','password':'tenfey2017@677'}
        print('开始登陆')
        yield scrapy.FormRequest(url='https://admin.renqitv.cn/user/checkPassword',meta={'cookiejar':response.meta['cookiejar']},formdata=data,callback=self.isLogin)
        print('数据已返回')


    def isLogin(self,response):
        b=json.loads(response.body)
        print(b)
        if 0 == b['errno'] :
            print('登陆成功')
            data = {
               'page': '1',
               'rows': '20'
            }
            yield scrapy.FormRequest(url='https://admin.renqitv.cn/userInfo/userfeedback',meta={'cookiejar':response.meta['cookiejar']}, formdata=data, callback=self.Customer)



    def Customer(self,response):
        b=json.loads(response.body)
        print(b)
        print("数据已返回")
