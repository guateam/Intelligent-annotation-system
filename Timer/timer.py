import datetime
from threading import Timer

from API.db import Database
from CollaborativeFiltering.cf import set_similarity_vec


def cf():
    """
    计算cf矩阵
    :return:
    """
    db = Database()
    user_count=db.count({'is_del':0},'user')
    matrix = []
    article=db.get({},'article',0)
    for value in article:
        data = db.get({'article_id': value['id']}, 'user_personas',0)
        list = [0.5] * user_count
        for user in data:
            list[user['user_id'] - 1] = user['weight']
        matrix.append(list)
    print(matrix)
    print(set_similarity_vec(matrix, "../CollaborativeFiltering/item_simi.txt"))


def timer(time, count=0):
    count += 1
    print('[' + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '] 第' + str(count) + '次运行')
    cf()
    Timer(time, timer, (time, count,)).start()


if __name__ == '__main__':
    timer(5)
