def cosine_similarity(vector1, vector2):
    """
    计算出余弦相似度
    :param vector1: 用户的评分矩阵，一维
    :param vector2: 某个其他用户的评分矩阵，一维
    :return: 用户和某个用户的兴趣相似度
    """
    dot_product = 0.0
    norm_a = 0.0
    norm_b = 0.0
    for a, b in zip(vector1, vector2):
        dot_product += a * b
        norm_a += a ** 2
        norm_b += b ** 2
    if norm_a == 0.0 or norm_b == 0.0:
        return 0
    else:
        return round(dot_product / ((norm_a ** 0.5) * (norm_b ** 0.5)) * 100, 2)


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


def most_interest(similar_vec, rate_vec, k=1, m=1):
    """
    获取目标用户最感兴趣的几个对象
    :param similar_vec: 其他用户和目标用户的兴趣相似度矩阵，一维
    :param rate_vec: 用户的评分矩阵，二维，一维对应某用户，一维对应该用户的评分
    :param k: 选取其他用户的个数，按相似度程度降序排列
    :param m: 输出的元组个数
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

    print(len(together))
    print(together[0][1])
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


def cf(item_vec, rate_vec, k=1, m=1):
    """
    用cf算法推荐对象，默认为向量的第一个用户提供推荐
    :param item_vec: 对象的向量
    :param rate_vec: 评分的向量
    :param k: 选取其他用户的个数，按相似度程度降序排列
    :param m: 输出的元组个数
    :return: 推荐的对象
    """
    # 相似度矩阵，待计算
    similar_vec = []
    for i in range(len(rate_vec)):
        if i == 0:
            # 以第一个用户为目标用户，第一次循环计算自己的相似度，adjusted_cosin算法得到的值越小，相似度越大，这里设置为0
            # 表示最大相似度
            similar_vec.append(0)
        else:
            # 以第一个用户为目标用户，计算其他用户的相似度
            similar_vec.append(cosine_similarity(rate_vec[0], rate_vec[i]))

    # 获取目标用户最感兴趣的对象类型
    most_interest_vec = most_interest(similar_vec[1:], rate_vec[1:], k, m)
    # 输出类型
    # 当用户基数少的时候，由于cos计算结果可能都很大，即使选取最相似的其他用户进行推荐，也会形成推荐不准确
    # 比如这个例子下的结果"财经",目标用户对财经的评价很低，但是依然推荐了财经
    data = []
    for i in range(m):
        data.append(item_vec[most_interest_vec[i][0]])
    return data


# 以下为使用样例

# 用户id列表
uec = [1, 2, 3, 4]
# 对象类型
ivec = ["体育", "游戏", "财经", "军事", "娱乐"]
# 每个用户对每个对象类型的评分(在本系统中，对象是文章类型，评分是偏好程度，偏好程度可以根据点赞数量，浏览次数等等数据获得)
rvec = [
    [1, 3, 0.4, 2.2, 1.3],
    [0.8, 0.7, 1.5, 1.7, 3],
    [1.6, 0.4, 2.3, 1, 1.5],
    [0.7, 1.6, 1.1, 1.2, 0.3],
]

print(cf(ivec, rvec, 2, 2))
