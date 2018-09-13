import jieba


def word_segmentation(sentence, hmm=True):
    """
    对句子进行分词
    :param sentence: 待分词的句子
    :param hmm: 是否开启新词发现
    :return: 分词结果列表，非list，可迭代
    """
    jieba.enable_parallel(4)  # 使用4进程运行
    seg_list = jieba.cut(sentence, HMM=hmm)  # 分词
    return seg_list


if __name__ == '__main__':
    for word in word_segmentation('我们中出了一个叛徒', hmm=False):
        print(word, end='/')
