# 页面解析器
# 用于从源码中选出需要的数据
import re

from pyquery import PyQuery


class Parser(object):

    def __init__(self):
        self.db = None  # 存储url的数据库
        self.data = dict()

    def parse_book_index(self, html):
        if html is not None:  # 确认html存在
            doc = PyQuery(html)  # 使用PyQuery加载并格式化html文档
            # 尝试获取书籍评分
            try:
                rate = float(doc.find('#interest_sectl > div > div.rating_self.clearfix > strong').text())
                if rate >= 7.0:  # 选择评分>=7.0的图书
                    # 获取短评页面的URL
                    pl_url = doc.find(
                        '#content > div > div.article > div.related_info > div.mod-hd > h2 > span.pl > a').attr('href')
                    yield pl_url  # 返回短评页面的URL
            except ValueError:
                # 如果没有评分则跳过此书
                pass

            books = doc.find('#db-rec-section > div > dl:not(.clear)').items()  # 获取书籍列表
            for book in books:
                book_url = book.find('dd > a').attr('href')  # 获取书籍url
                # self.db.insert_book(book_url)  # 把书籍添加到数据库
        else:
            print('Index is not exist.')

    def parse_book_comments(self, html):
        if html is not None:  # 确认源码存在
            doc = PyQuery(html)  # 使用PyQuery加载并格式化html文档
            comments = doc.find('#comments > ul:nth-child(1) > li').items()
            for comment in comments:
                self.data = {
                    'text': comment.find('div.comment > p > span').text(),  # 获取评价内容
                    'agree': int(comment.find('div.comment .comment-vote > span').text()),  # 获取赞同数
                    'star': int(re.findall(r'[0-9.]',
                                           comment.find('div.comment > h3 > span.comment-info > span[title]').attr(
                                               'class'))[0]),  # 获取星星数
                }  # 将要返回的数据
                yield self.data


if __name__ == '__main__':
    from Crawler.downloader import Downloader
    import json

    d = Downloader()
    p = Parser()
    for comment_url in p.parse_book_index(d.download('https://book.douban.com/subject/4011670/')):
        for data in p.parse_book_comments(d.download(comment_url)):
            print(json.dumps(data, ensure_ascii=False, indent=4))
