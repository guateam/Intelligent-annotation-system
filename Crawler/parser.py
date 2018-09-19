# 页面解析器
# 用于从源码中选出需要的数据
from pyquery import PyQuery


class Parser(object):

    def __init__(self):
        self.item = {}  # 用于存储数据的字典

    def parse_book_index(self, html):
        if html:
            doc = PyQuery(html)  # 使用PyQuery加载并格式化html文档
            book_name = doc.find('#wrapper > h1 > span').text()
            try:
                # 获取书籍评分
                rate = float(doc.find('#interest_sectl > div > div.rating_self.clearfix > strong').text())
            except ValueError:
                # 如果书籍没有评分则认为评分为0
                rate = 0.0
            book_list = []  # 推荐书籍列表
            books = doc.find('#db-rec-section > div > dl:not(.clear)').items()  # 选择书籍列表
            for book in books:
                book_url = book.find('dd > a').attr('href')  # 获取书籍url
                book_list.append(book_url)  # 将url加入书籍列表
            if rate >= 7.0:
                print('评分: {rate}, 书名: {book}'.format(rate=rate, book=book_name))
            return book_list
        else:
            return False


if __name__ == '__main__':
    from Crawler.downloader import Downloader

    d = Downloader()
    p = Parser()
    url_list = ['https://book.douban.com/subject/30305583']
    for url in url_list:
        page_source = d.download(url)
        url_list += p.parse_book_index(page_source)
