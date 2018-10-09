from TextFeatureExtraction.WordSegmentation import pred
import numpy as np

def cosine_similarity(vector1, vector2):
    """
    计算出余弦相似度,越接近1越相似
    :param vector1: 用户的评分矩阵，一维
    :param vector2: 某个其他用户的评分矩阵，一维
    :return: 用户和某个用户的兴趣相似度
    """
    dot_product = 0.0
    norm_a = 0.0
    norm_b = 0.0
    for a, b in zip(vector1, vector2):
        dot_product += (a * b)
        norm_a += a ** 2
        norm_b += b ** 2
    if norm_a == 0.0 or norm_b == 0.0:
        return 0
    else:
        norm_a = norm_a ** 0.5
        norm_b = norm_b ** 0.5
        return round(dot_product / (norm_a*norm_b), 4)


def set_similarity_vec(vec,name = "similarity_vector.txt"):
    """
    计算相似矩阵
    :param vec: 待算的的向量，可以为 用户评分列表或者文章列表
    :param name: 存储的文件名称
    :return: 返回规模为 用户*用户 或者 文章*文章 的相似度矩阵
    """
    simi_vec = [[0 for i in range(len(vec))] for j in range(len(vec)) ]
    f = open(name,"w")
    for i in range(len(vec)):
        for j in range(len(vec)):
            simi_vec[i][j] = cosine_similarity(vec[i], vec[j])
            f.write(str(simi_vec[i][j])+",")
        f.write("\n")
    f.close()
    return simi_vec


def read_similarity_vec(dir = "similarity_vector.txt"):
    """
    读取文件中存储的相似度矩阵
    :param dir: 读取的文件路径，默认为本目录下的similarity_vector.txt
    :return: 相似度矩阵
    """
    with open(dir,'r') as f:
        lines = f.readlines()
        simi_vec = [[0 for i in range(len(lines))] for j in range(len(lines)) ]
        for i in range(len(lines)):
            line = lines[i].split(",")
            for j in range(len(line)-1):
                simi_vec[i][j] = float(line[j])
    return simi_vec


def interest_value(similar, rate_vec):
    """
    获取兴趣程度，作为protected方法使用
    :param similar: 该用户和目标用户的兴趣相似度,数字
    :param rate_vec: 该用户的评分矩阵，一维
    :return: 每个评价对象的兴趣程度 ,一维
    """
    interest_vec = []
    for i in range(len(rate_vec)):
        interest_vec.append(similar * rate_vec[i])
    return interest_vec


def most_similar(simi_vec,idx):
    """
    根据相似度矩阵获取最相似的项
    :param simi_vec: 相似度矩阵
    :param idx: 比较的对象下标
    :return: 最相似项的下标
    """
    most_val = 10000
    most_idx = 0
    for i in range(len(simi_vec[idx])):
        if(abs(simi_vec[idx][i]-1) < most_val ):
            if(idx != i):
                most_val = abs(simi_vec[idx][i]-1)
                most_idx = i
    return most_idx


def most_interest(similar_vec, rate_vec, k=1, m=1):
    """
    获取目标用户最感兴趣的几个对象
    :param similar_vec: 其他用户和目标用户的兴趣相似度矩阵，一维
    :param rate_vec: 用户的评分矩阵，二维，一维对应某用户，一维对应该用户的评分
    :param k: 选取其他用户的个数，按相似度程度降序排列,默认为1
    :param m: 输出的元组个数，默认为1
    :return: 元组，格式为 (评论对象下标，兴趣度)
    """

    # 兴趣数组，待计算
    total_interest = []
    # 初始化长度，长度为评价向量的长度，数组内每一个元素对应每个对象的兴趣程度
    for i in range(len(rate_vec[0])):
        total_interest.append(0)

    # 将相关的数据整合到同一个数据结构内，便于之后的处理
    together = sorted(list(zip(list(zip(range(len(similar_vec)), similar_vec)), rate_vec)), key=lambda item: item[0][1])
    # 选取前k个最相关的其他用户
    together = together[0:k]

    # 根据公式计算  用户u对物品i的感兴趣程度  P(u,i) = ∑S(u,k)∩N(i)  Wuv*Rvi
    # S(u, K)包含和用户u兴趣最接近的K个用户， N(i)是对物品i有过行为的用户集合，
    # w_uv是用户u和用户v的兴趣相似度， r_vi代表用户v对物品i的兴趣度
    for i in range(len(together)):
        now_vec = interest_value(together[i][0][1], together[i][1])
        for j in range(len(now_vec)):
            total_interest[j] += now_vec[j]

    zip_interest = dict(zip(range(len(total_interest)), total_interest))
    # 排序，选出最感兴趣的m类物品
    sorted_interest = sorted(zip_interest.items(), key=lambda item: item[1], reverse=True)
    return sorted_interest[:m]


def cf(self_vec,others_vec,k=1, m=1,item_vec = []):
    """
    用cf算法推荐对象
    :param self_vec: 需要进行推荐的用户评分矩阵,一维[ , , ]
    :param others_vec: 其他用户的评分矩阵,二维[ [] , [] ]
    :param k: 选取其他用户的个数，按相似度程度降序排列
    :param m: 输出的元组个数
    :param item_vec: 如果该参数存在，则直接输出推荐对象对应下标的名称，否则输出下标
    :return: 推荐的对象
    """
    # 相似度矩阵，待计算
    similar_vec = []
    rate_vec = [self_vec]+others_vec
    for i in range(len(rate_vec)):
        if i == 0:
            # 以第一个用户为目标用户，第一次循环计算自己的相似度，adjusted_cosin算法得到的值越接近1，相似度越大，这里设置为1-1=0
            # 表示最大相似度
            similar_vec.append(0)
        else:
            # 以第一个用户为目标用户，计算其他用户的相似度
            similar_vec.append(abs(cosine_similarity(rate_vec[0], rate_vec[i])-1))

    # 获取目标用户最感兴趣的对象类型
    most_interest_vec = most_interest(similar_vec[1:], rate_vec[1:], k, m)
    # 输出类型
    # 当用户基数少的时候，由于cos计算结果可能都很大，即使选取最相似的其他用户进行推荐，也会形成推荐不准确
    # 比如这个例子下的结果"财经",目标用户对财经的评价很低，但是依然推荐了财经
    data = []
    for i in range(m):
        if len(item_vec)!=0:
            data.append(item_vec[most_interest_vec[i][0]])
        else:
            data.append(most_interest_vec[i][0])
    return data


def item_cf(dir,target):
    """
    基于物品的cf算法
    :param dir: 要读取的物品相似度矩阵文件
    :param target: 为某个物品推荐，该物品的下标
    :return: 推荐的物品下标
    """
    simi_vec = read_similarity_vec(dir)
    idx = most_similar(simi_vec,target)
    return idx

# 以下为基于用户的使用样例

# 用户id列表
uec = [1, 2, 3, 4]
# 对象类型
ivec = ["体育", "游戏", "财经", "军事", "娱乐"]
# 每个用户对每个对象类型的评分(在本系统中，对象是文章类型，评分是偏好程度，偏好程度可以根据点赞数量，浏览次数等等数据获得)
self_rvec = [1, 3, 0.4, 2.2, 1.3]
rvec = [
    [0.9, 3.3, 0.7, 1.9, 1],
    [0.8, 0.7, 1.5, 1.7, 3],
    [1.6, 0.4, 2.3, 1.0, 1.5],
    [0.7, 1.6, 1.1, 1.2, 0.3],
]
print("输出名称：")
print(cf(self_rvec, rvec, 2, 2,ivec))


# 以下是item_cf的使用样例
# 首先建立物品的相似矩阵(根据物品的评分矩阵来获得，物品评分矩阵是所有用户对该物品的评分合集)
item = [
    [1,2,3,1,0],
    [3,2,1,2,1],
    [1,1,2,2,1],
    [2,1,2,3,1]
]
set_similarity_vec(item,"item_simi.txt")
print(item_cf("item_simi.txt",0))

print(read_similarity_vec())


