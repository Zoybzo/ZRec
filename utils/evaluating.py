def recall(train, test, rank, N):
    '''
    召回率 描述有多少比例的评分记录包含在最终的推荐列表中
    :param train:
    :param test:
    :param N:
    :return:
    '''
    hit = 0
    all = 0
    for user in train.keys():
        tu = test[user]  # 用户在测试集上喜欢的物品的集合
        # rank = getRec(user, N)  # 模型得到的结果
        for item, pui in rank:
            if item in tu:
                hit += 1
        all += len(tu)
    return hit / (all * 1.0)
