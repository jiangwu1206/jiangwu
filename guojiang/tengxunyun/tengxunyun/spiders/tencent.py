# -*- coding: utf-8 -*-
import scrapy
from selenium import webdriver
import time
import json
import execjs
import math
from tengxunyun.items import TengxunyunItem


def _jqjsp(dict):
    return dict



class TencentSpider(scrapy.Spider):
    
    #'''
    stat_start_time=time.strftime('%Y-%m-%d',time.localtime())+" 00:00"
    stat_end_time=time.strftime('%Y-%m-%d',time.localtime())+" 23:59"
    '''
    stat_start_time="2018-04-19 00:00"
    stat_end_time="2018-04-24 23:59"
    #'''
    tk=''
    page_no='1'
    totalnum=''

    def get_cookie(self):
        browser = webdriver.Chrome(r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
        browser.get("https://cloud.tencent.com/login")
        time.sleep(3)
        qq=browser.find_element_by_xpath('//*[@id="loginBox"]/div/div/div[4]/div[1]/div/a[1]')
        qq.click()
        time.sleep(1)
        browser.switch_to_frame("qc_ptlogin_iframe")
        u=browser.find_element_by_id("u")
        u.clear()
        u.send_keys("账号")
        p=browser.find_element_by_id("p")
        p.clear()
        p.send_keys("密码")
        browser.find_element_by_class_name("btn").click()
        time.sleep(2)
        print("登陆成功")
        skey=browser.get_cookie('skey')['value']
        ck=browser.get_cookies()
        js="""
        var getACSRFToken = function (skey) {
                if(!skey){ return ''}
                var hash = 5381
                for (var i = 0, len = skey.length; i < len; ++i) { hash += (hash << 5) + skey.charCodeAt(i) }
                return hash & 0x7fffffff
                } 
        """
        rjs=execjs.compile(js)
        self.tk=str(rjs.call("getACSRFToken",skey))
        return ck
    
    
    name = 'tencent'
    allowed_domains = ['tencent.com']
    
    def start_requests(self):
        cookie=self.get_cookie()
        sdate=input("请输入开始日期如2018-01-01:")
        edate=input("请输入结束日期如:2018-01-01:")
        try:
            time.strptime(sdate,"%Y-%m-%d")
            time.strptime(edate,"%Y-%m-%d")
            self.stat_start_time=sdate+" 00:00"
            self.stat_end_time=edate+" 23:59"
        except:
            print("日期有误")
            print("程序将使用系统当前日期")
        
        uri='https://lvbs.cloud.tencent.com/livesdk/Live_Sdk_UploadUserStreamList' \
        +'?g_tk='+self.tk+'&_format=jsonp&type=0&page_size=100&callback=_jqjsp&stat_start_time='+self.stat_start_time \
        +'&stat_end_time='+self.stat_end_time+'&page_no='+self.page_no
        
        yield scrapy.Request(url=uri,callback=self.txy,cookies=cookie,dont_filter = True)   
            
    def txy(self,response):
        txydata = str(response.body ,encoding = "utf-8")
        txydict=eval(txydata)
        
        if 'data' in txydict :
            data=txydict['data']
            self.totalnum=data['totalnum']
            print(self.totalnum)
            data=data['data']
            
            for i in data :
                item=TengxunyunItem()
            
                item['bizid']=i['bizid']
                item['appid']=i['appid']
                item['stream_id']=i['stream_id']
                item['id_hash']=i['id_hash']
                item['u64_begin_time']=i['u64_begin_time']
                item['str_device_type']=i['str_device_type']
                item['u32_network_type']=i['u32_network_type']
                item['str_server_ip']=i['str_server_ip']
                item['u32_conn_server_time']=i['u32_conn_server_time']
                item['u32_video_reso']=i['u32_video_reso']
                item['u32_video_bitrate']=i['u32_video_bitrate']
                item['update_time']=i['update_time']
                yield item
            
        self.page_no=int(self.page_no)+1
        print(self.page_no)
        MaxPageNO=int(math.ceil(int(self.totalnum)/100))
        
        if(self.page_no>MaxPageNO):
            print("退出")
            return
           
        self.page_no=str(self.page_no)
        uri='https://lvbs.cloud.tencent.com/livesdk/Live_Sdk_UploadUserStreamList' \
            +'?g_tk='+self.tk+'&_format=jsonp&type=0&page_size=100&callback=_jqjsp&stat_start_time='+self.stat_start_time \
            +'&stat_end_time='+self.stat_end_time+'&page_no='+self.page_no
        yield scrapy.Request(url=uri,callback=self.txy,dont_filter = True)