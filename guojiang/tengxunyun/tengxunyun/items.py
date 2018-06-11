# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TengxunyunItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    bizid=scrapy.Field()
    appid=scrapy.Field()
    stream_id=scrapy.Field()
    id_hash=scrapy.Field()
    u64_begin_time=scrapy.Field()
    str_device_type=scrapy.Field()
    u32_network_type=scrapy.Field()
    str_server_ip=scrapy.Field()
    u32_conn_server_time=scrapy.Field()
    u32_video_reso=scrapy.Field()
    u32_video_bitrate=scrapy.Field()
    update_time=scrapy.Field()
