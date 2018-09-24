# 定义异常


class QueueEmptyError(Exception):

    def __init__(self):
        Exception.__init__(self)  # 初始化为异常

    def __str__(self):
        return repr('队列中没有未检测的URL')  # 异常描述
