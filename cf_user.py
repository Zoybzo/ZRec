





# 处理数据
def splitData(data, M, k, seed):
    test = []
    train = []
    random.seed(seed)
    for user, item in data:
        if random.randint(0, M) == k:
            test.append([user, item])
        else:
            train.append([user, item])
    return train, test

# 模型

## 用户相似度

## 用户对物品的兴趣

# 输出

# 评判
