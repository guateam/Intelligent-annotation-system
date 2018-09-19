# 页面下载器
# 用于下载包含所需数据的页面源码
import requests


class Downloader(object):

    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
        }  # 请求头信息

    def download(self, url):
        """
        下载页面源码
        :param url: 目标地址
        :return: 网页源码，失败时返回False
        """
        try:
            response = requests.get(url, headers=self.headers)  # 发送请求
            if response.status_code == requests.codes.ok:  # 判断响应状态
                page_source = response.text  # 获取网页源码
                return page_source  # 返回源码
            else:
                response.raise_for_status()  # 抛出异常状态
        except requests.exceptions.HTTPError as e:
            print(e)  # 打印出异常信息
            return False  # 返回False


# 测试异常处理
if __name__ == '__main__':
    dlr = Downloader()
    html = dlr.download(url='http://httpbin.org/status/404')
