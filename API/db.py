import pymysql


"""                      MYSQL信息                      """
MYSQL_HOST = 'localhost'
MYSQL_PORT = 3306
MYSQL_USER = 'root'
MYSQL_PASSWORD = ''
MYSQL_DB = 'IntelligentAnnotationSystem'
""" 以上为变量为演示所用，正式开发时请统一写入config文件后引入 """


class Database(object):
    # __init__方法将在类实例创建时执行，可用于完成数据库的初始化操作
    def __init__(self, host=MYSQL_HOST, port=MYSQL_PORT, user=MYSQL_USER, password=MYSQL_PASSWORD, db=MYSQL_DB):
        try:
            # 连接数据库，之后在类方法中使用 self.db 调用
            self.db = pymysql.connect(
                host=host,
                port=port,
                user=user,
                passwd=password,
                db=db,
                charset='utf8',
                cursorclass=pymysql.cursors.DictCursor
            )
        except pymysql.MySQLError as e:
            print(e.args)  # 这里将错误信息打印到控制台，实际开发时应该写入日志文件

    # __del__方法将在类实例被销毁时执行，此处用于关闭数据库，实际上python会自动完成关闭和清理操作
    def __del__(self):
        self.db.close()

    # 实现一个INSERT方法，此处将演示pyCharm常用的方法注释功能
    def insert(self, data, table):
        """
        将数据添加到表
        :param data: 待添加的数据，类型为dict
        :param table: 目标table的名称
        :return: 操作是否成功
        """
        # 构造键值成分
        keys = ', '.join(data.keys())
        values = ', '.join(['%s'] * len(data))
        # 插入数据
        try:
            with self.db.cursor() as cursor:
                # 构造sql语句
                sql_query = 'INSERT INTO %s (%s) VALUES (%s)' % (table, keys, values)
                cursor.execute(sql_query, tuple(data.values()))
            # 提交语句
            self.db.commit()
            return True
        except pymysql.MySQLError as e:
            print(e.args)
            return False
