import json
import re

from Crawler.crawler import Crawler
from Crawler.db import RedisClient
from Crawler.error import QueueEmptyError

LIST_UPPER_THRESHOLD = 30000  # 爬取的图书上限


class Getter(object):

    def __init__(self):
        self.redis = RedisClient()  # 加载任务队列
        self.crawler = Crawler()  # 加载爬虫

    def is_over_threshold(self):
        """
        判断图书数量是否超出了限制
        :return:
        """
        if self.redis.count() >= LIST_UPPER_THRESHOLD:
            return True
        else:
            return False

    def get_book_url(self):
        """
        从TOP250获取书籍列表
        :return:
        """
        print('Getting book URLs...')
        if not self.is_over_threshold():  # 如果没有达到上限
            book_list = self.crawler.crawl_home()  # 获取书籍列表
            if book_list is not None:  # 如果书籍列表不为空
                for book in book_list:
                    if re.match(r'https://book.douban.com/subject/.*', book):  # 检测书籍url格式
                        self.redis.add(book)  # 把书籍URL加入队列
        else:
            print('Queue is over threshold.')
            return

    def get_comments(self):
        """
        获取评论信息
        :return:
        """
        print('Getting comments...')
        try:
            while True:
                book_url = self.redis.pop()  # 尝试从队列中取出一本书
                comment_url, book_list = self.crawler.crawl_index(book_url)  # 对这本书进行解析
                if book_list is not None and not self.is_over_threshold():  # 如果书籍列表不为空并且队列没有达到上限
                    for book in book_list:
                        if re.match(r'https://book.douban.com/subject/.*', book):  # 检测书籍url格式
                            if self.redis.add(book) == 0:  # 把获取到的书籍加入队列
                                self.redis.done(book)  # 如果书籍已经存在则标记为完成
                if comment_url is not None:  # 如果成功获取到书评URL
                    data_list = self.crawler.crawl_comments(comment_url)  # 解析评论
                    # 显示评论信息
                    for data in data_list:
                        with open('data.json', 'a+') as f:
                            f.write(json.dumps(data, indent=4, ensure_ascii=False) + ',\n')
                    self.redis.done(book_url)  # 把书籍标记为已爬取
                else:
                    self.redis.delete(book_url)  # 从队列中删除不符合要求的书籍
        except QueueEmptyError:  # 捕获队列为空异常
            return  # 如果队列为空则结束程序

    def run(self):
        self.get_book_url()
        self.get_comments()
