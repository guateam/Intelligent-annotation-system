import re

from pyquery import PyQuery

from Crawler.utils import get_page, book_rules

"""
爬虫解析器
"""


class Crawler(object):

    @staticmethod
    def crawl_home():
        """
        解析豆瓣图书TOP250
        :return: 包含250图书URL的生成器
        """
        start_url = 'https://book.douban.com/top250?start={}'  # 豆瓣图书Top 250
        urls = [start_url.format(start) for start in range(0, 250, 25)]  # 构造10页的URL
        for url in urls:
            html = get_page(url)  # 获取页面
            if html:
                doc = PyQuery(html)  # 加载解析器
                a_tag_list = doc.find('a').items()  # 获取全部a标签
                for a_tag in a_tag_list:
                    book_url = a_tag.attr('href')  # 提取a标签的href属性
                    if re.match(r'https://book.douban.com/subject/.*', book_url):  # 利用正则表达式选出书籍详情页
                        yield book_url  # 返回书籍详情页的URL

    @staticmethod
    def crawl_index(url):
        """
        解析书籍详情页, 对符合条件的书籍返回短评页URL和更多书籍列表
        :param url: 书籍页URL
        :return: 短评页URL和更多书籍列表
        """
        html = get_page(url)  # 获取页面
        if html:
            doc = PyQuery(html)  # 加载解析器
            book_name = doc.find('#wrapper > h1 > span').text()  # 获取书籍标题
            book_rate = doc.find('#interest_sectl > div > div.rating_self.clearfix > strong').text()  # 获取书籍分数
            dls = doc.find('#db-rec-section > div > dl').items()
            more_book_list = []  # 更多书籍列表
            for dl in dls:
                more_book_url = dl.find('dd > a').attr('href')  # 获取更多书籍的URL
                more_book_list.append(more_book_url)  # 将URL加入更多书籍列表
            print(book_name + ', 豆瓣评分: ' + (book_rate if book_rate != '' else '没有评分'))  # 显示书籍信息
            if book_rules(book_rate):  # 选出符合筛选规则的书
                comments_url = doc.find('#content > div > div.article > div.related_info > div.mod-hd > h2 > span.pl '
                                        '> a').attr('href')  # 获取短评页URL
                # print('短评URL: ', comments_url)  # 显示短评页URL
            else:
                comments_url = None  # 对于不符合要求的书，返回None
            return comments_url, more_book_list  # 返回短评页URL和更多书籍列表
        else:
            return None, None

    @staticmethod
    def crawl_comments(comments_url):
        """
        解析热评前5页
        :param comments_url: 热评页URL
        :return: 包含短评数据的生成器
        """
        urls = [(comments_url + '?p={}'.format(page)) for page in range(1, 6)]  # 构造热评前5页的URL
        for url in urls:
            html = get_page(url)  # 获取页面
            if html:
                doc = PyQuery(html)  # 加载解析器
                lis = doc.find('#comments > ul:nth-child(1) > li').items()  # 获取列表信息
                for li in lis:
                    rate_class = li.find(
                        'div.comment > h3 > span.comment-info > span.user-stars.allstar50.rating').attr(
                        'class')  # 获取rate的class属性
                    comment_data = {
                        # 解析用户昵称
                        'nickname': li.find('div.comment > h3 > span.comment-info > a').text(),
                        # 解析rate值, 如果没有则认为是0
                        'rate': int(re.findall(r'[0-9]', rate_class)[0]) if rate_class is not None else 0,
                        # 解析"有用的"数值
                        'useful': li.find('div.comment > h3 > span.comment-vote > span').text(),
                        # 解析评论内容
                        'text': li.find('div.comment > p > span').text(),
                        # 解析评论时间
                        'time': li.find('div.comment > h3 > span.comment-info > span:nth-child(3)').text(),
                    }
                    yield comment_data


# 测试
if __name__ == '__main__':
    c = Crawler
    c.crawl_comments('https://book.douban.com/subject/1770782/comments/hot')
