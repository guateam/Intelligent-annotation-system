# 爬虫项目的调度器
# 用于协调爬虫各部分功能
from Crawler.db import RedisClient
from Crawler.parser import Parser
from Crawler.downloader import Downloader


class Schedule(object):

    def __init__(self):
        self.db = RedisClient()  # 用于存储目标队列的数据库
        self.downloader = Downloader()  # 页面下载器
        self.parser = Parser()  # 页面解析器
        # self.saver = Saver()  # 数据存储器
