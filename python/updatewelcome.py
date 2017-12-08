#!/usr/bin/env python
# coding: utf-8
import commands

import requests
import json
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
"""
获取天气数据
获取每日一句数据
将所需数据写入文件
执行shell命令,将文件内容写入/etc/motd
"""

if __name__ == '__main__':
    try:
        daily = open("daily.txt", 'w')
        weatherUrl = "http://www.sojson.com/open/api/weather/json.shtml?city=深圳"
        r = requests.get(weatherUrl)
        if r.status_code == 200:
            resultJson = json.loads(r.text)
            data = resultJson['data']
            # 空气质量
            quality = data['quality']
            # 湿度
            humidity = data['shidu']
            pm25 = data['pm25']
            # 户外
            ganmao = data['ganmao']
            today = data['forecast'][0]
            # 最高气温
            high = today['high']
            # 最低气温
            low = today['low']
            # 建议
            notice = '[' + today['type'] + ']' + today['notice']
            # 日期
            date = today['date']

            daily.write("今天是:" + date + '\n')
            daily.write("湿度:" + humidity + '\n')
            daily.write("pm25:" + str(pm25) + '\n')
            daily.write(high + '\n')
            daily.write(low + '\n')
            daily.write("空气质量:" + quality + '\n')
            daily.write(notice + '\n')
            daily.write("户外建议:" + ganmao + '\n')

        # 每日一句
        url = "http://open.iciba.com/dsapi/"
        r = requests.get(url)
        if r.status_code == 200:
            resultJson = json.loads(r.text)
            note = resultJson['note']
            content = resultJson['content']
            daily.write(content + '\n')
            daily.write(note + '\n')
        daily.close()
        commands.getstatusoutput('cp daily.txt  /etc/motd')
    except:
        pass