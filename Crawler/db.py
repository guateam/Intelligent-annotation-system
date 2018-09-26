import redis

from Crawler.error import QueueEmptyError

# 数据库信息
REDIS_HOST = 'localhost'
REDIS_PORT = 6379
REDIS_PASSWORD = None

# 键名
REDIS_KEY = 'books'

# 分数
MAX_SCORE = 100
MIN_SCORE = 0


class RedisClient(object):

    def __init__(self, host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASSWORD):
        """
        初始化
        :param host: Redis 地址
        :param port: Redis 端口
        :param password: Redis 密码
        """
        self.db = redis.StrictRedis(host=host, port=port, password=password, decode_responses=True)

    def add(self, url, score=MAX_SCORE):
        """
        添加url，分数设置为100
        :param score: 分数
        :param url: url
        :return: 添加结果，成功为1，失败为None
        """
        if not self.db.zscore(REDIS_KEY, url):  # 查询是否已存在
            return self.db.zadd(REDIS_KEY, score, url)  # 插入集合，分数设置为最大值

    def done(self, url):
        """
        把url标记为已完成，分数-100
        :param url: url
        :return: 修改后的分数
        """
        score = self.db.zscore(REDIS_KEY, url)  # 获取分数
        if score > MIN_SCORE:  # 如果分数大于最小值
            print('图书链接 {} , 标记为已完成.'.format(url))
            return self.db.zincrby(REDIS_KEY, url, -MAX_SCORE)  # 分数减去最大值

    def exists(self, url):
        """
        判断是否存在
        :param url: url
        :return: 是否存在
        """
        return self.db.zscore(REDIS_KEY, url) is not None

    def count(self):
        """
        获取数量
        :return: 数量
        """
        return self.db.zcard(REDIS_KEY)  # 获取数量

    def all(self):
        """
        获取全部url
        :return: 全部url列表
        """
        return self.db.zrangebyscore(REDIS_KEY, MIN_SCORE, MAX_SCORE)  # 获取分数在最大值和最小值范围内的url

    def pop(self):
        """
        取出一个没有爬取过的url，如果没有则抛出异常
        :return: url
        """
        result = self.db.zrangebyscore(REDIS_KEY, MAX_SCORE, MAX_SCORE)  # 获取分数为最大值的结果列表
        if len(result):
            return result.pop()  # 如果列表中有数据，取出一个
        else:
            raise QueueEmptyError  # 抛出队列为空异常

    def clear(self):
        """
        清空集合
        :return: 删除的url数量
        """
        return self.db.zremrangebyscore(REDIS_KEY, MIN_SCORE, MAX_SCORE)  # 删除所有成员

    def delete(self, url):
        """
        删除url
        :param url: URL
        :return:
        """
        print('图书链接 {} 已从队列中移除.'.format(url))
        return self.db.zrem(REDIS_KEY, url)  # 删除url
