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
    postil=db.get({},'postil',0)
    for value in postil:
        data = db.get({'postil_id': value['id']}, 'user_personas_postil',0)
        list = [0.5] * user_count
        for user in data:
            list[user['user_id'] - 1] = user['weight']
        matrix.append(list)
    print(matrix)
    print(set_similarity_vec(matrix, "../CollaborativeFiltering/item_simi_postil.txt"))


def timer(time, count=0):
    count += 1
    print('[' + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '] 第' + str(count) + '次运行@批注的ItemCF算法')
    cf()
    Timer(time, timer, (time, count,)).start()


if __name__ == '__main__':
    timer(5)
