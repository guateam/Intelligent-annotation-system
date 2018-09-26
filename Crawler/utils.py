import requests

"""
工具集
"""


def get_page(url):
    """
    下载页面源码
    :param url: 目标地址
    :return: 网页源码
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/69.0.3497.100 Safari/537.36',
    }  # 请求头信息
    res = requests.get('http://localhost:5555/random')
    proxies = {
        'http': 'http://46.55.82.193:51948',
        'https': 'http://46.55.82.193:51948',
    }
    if res.status_code == requests.codes.ok:
        ip = res.text
        proxies = {
            'http': 'http://{}'.format(ip),
            'https:': 'http://{}'.format(ip),
        }
        print('当前正在使用代理:', proxies['http'])
    page_source = None  # 定义返回值
    # 尝试发送请求
    try:
        response = requests.get(url, headers=headers, proxies=proxies)
        if response.status_code == requests.codes.ok:  # 判断响应状态
            page_source = response.text  # 获取网页源码
        else:
            response.raise_for_status()  # 抛出异常状态
    except requests.exceptions.HTTPError as e:
        print(e)  # 打印出异常信息
    except requests.exceptions.ProxyError:
        return get_page(url)
    return page_source  # 返回源码


def book_rules(rate):
    """
    书籍筛选规则
    :param rate: 评分
    :return: 是否符合条件
    """
    try:
        rate = float(rate)  # 尝试将分数转换为float
        return rate >= 8.0  # 返回评分超过8.0的书
    except ValueError:
        return False  # 若触发异常表示没有评分, 则认为不符合条件


if __name__ == '__main__':
    url = 'https://www.baidu.com/s?wd=ip'
    html = get_page(url)
    print(html)
