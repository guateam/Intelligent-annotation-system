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
        'Host': 'book.douban.com',
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Referer': 'https://www.douban.com/',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cookie': 'bid=7qDrst2S3JQ; gr_user_id=6f410b34-9f84-4438-bf98-a1c403300fbe; __yadk_uid=pL0jIFv3V0EcNB18kLI3T17BpppQhStN; _vwo_uuid_v2=DFBA169972CE057E99C81ECD942BB8C35|516291bf5ce6334df2e2ac96ca79f9af; viewed="30237176_30305583_30282895_1017143_1770782"; as="https://sec.douban.com/b?r=https%3A%2F%2Fbook.douban.com%2Fsubject%2F30237176%2F%3Ficn%3Dindex-editionrecommend"; ps=y; dbcl2="185024174:mZ6vHevmaEk"; ck=Ar42; _pk_ref.100001.3ac3=%5B%22%22%2C%22%22%2C1537876087%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D; _pk_id.100001.3ac3=0bc963ed900a4f7f.1537861262.2.1537876087.1537867135.; _pk_ses.100001.3ac3=*; gr_session_id_22c937bbd8ebd703f2d8e9445f7dfd03=094dae56-7e15-428d-8105-3976aaa6a6d0; gr_cs1_094dae56-7e15-428d-8105-3976aaa6a6d0=user_id%3A1; gr_session_id_22c937bbd8ebd703f2d8e9445f7dfd03_094dae56-7e15-428d-8105-3976aaa6a6d0=true',
    }  # 请求头信息
    res = requests.get('http://localhost:5555/random')
    proxies = None
    if res.status_code == requests.codes.ok:
        ip = res.text
        proxies = {
            'http': 'http://{}'.format(ip),
            'https:': 'http://{}'.format(ip),
        }
        print('当前正在使用代理: ', proxies['http'])
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
