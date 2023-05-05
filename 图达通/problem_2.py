#question a
'''
1.给定一个整数列表stones和一个整数d，编写一个函数F，用于查找其中一对石头（即2个石头），
它们的重量差为d。如果存在这样的一对石头，则返回包含两个石头的元组；如果不存在这样的一对石头，则返回None。

2.函数F的输入参数为stones和d，其中stones是一个整数列表，表示每个石头的重量；d是所需的重量差。

3.函数F的输出为一个包含两个整数的元组，表示符合条件的石头对；如果不存在这样的一对石头，则返回None。

'''

#question b
## b.1(第一小问)
def find_stone_pair(stones, d):
    # 创建哈希表来存储石头的重量
    weights = {}

    # 遍历所有石头
    for stone in stones:
        # 检查哈希表中是否存在一个石头的重量等于当前石头的重量加上D或者减去D
        if stone + d in weights:
            return (stone, stone + d)
        elif stone - d in weights:
            return (stone - d, stone)

        # 把当前石头的重量添加到哈希表中
        weights[stone] = True

    # 没有找到符合条件的一对石头
    return None
## b.2(第二小问)
'''
上述代码使用了一个哈希表来存储石头的重量，因此空间复杂度取决于哈希表中需要存储多少个键值对。
在最坏情况下，所有的石头都不相同，那么哈希表中需要存储N个键值对。因此，空间复杂度为O(N)。
时间复杂度也为O(N)
'''

# b.3(第三小问)
'''
上述代码即满足了该要求
'''

## b.4(第4小问)
##4.a
'''
空的石头列表：[]
预期输出结果：None

只有一个石头的列表：[5]
预期输出结果：None

所有石头重量都相等的列表且d!=0：[2, 2, 2, 2, 2] 
预期输出结果：None

所有石头重量都小于D的列表：[1, 2, 3, 4, 5], d = 10
预期输出结果：None

所有石头重量都大于D的列表：[20, 30, 40, 50], d = 10
预期输出结果：(20,30)

有多对符合条件的石头：[1, 2, 3, 4, 5], d = 2
预期输出结果：(1,3)

没有符合条件的石头对：[1, 2, 3, 4, 5], d = 10
预期输出结果：None

'''
'''
测试样例的输入方式：
第一行为输入的所有石头权重列表
第二行为需要找到的权重差值

下面是一个样例：
输入：
20 30 40 50
10

表示输入的石头权重列表为[20,30,40,50],我们需要找到一组石头对，他们的差异值为10，比如(20,30),(30,40)都可以，任意返回一个即可
'''
#b.4 验证测试样例，具体测试情况可以见主函数
class Test_sample:
    def __init__(self,stones_weights,differ,ans):
        self.stones_weights=stones_weights
        self.differ=differ
        self.ans=ans

test_samples = [
        Test_sample([], 1, None),
        Test_sample([5], 2, None),
        Test_sample([1, 2, 3, 4, 5], 10, None),
        Test_sample([20, 30, 40, 50], 10, (20, 30)),
        Test_sample([1, 2, 3, 4, 5], 2, (1, 3)),
        Test_sample([1, 2, 3, 4, 5], 10, None)
    ]

#Question C代码
def find_stone_pairs(stones, d):
    # 步骤1：创建一个空字典，用于存储石头重量和索引
    stone_dict = {}
    for i in range(len(stones)):
        if stones[i] not in stone_dict:
            stone_dict[stones[i]] = []
        stone_dict[stones[i]].append(i)

    # 步骤2：查找所有重量差为D的石头对
    stone_pairs = set()
    for i in range(len(stones)):
        if (stones[i] + d) in stone_dict:
            for j in stone_dict[stones[i] + d]:
                if i != j:
                    stone_pairs.add(tuple(sorted([i, j])))
        if (stones[i] - d) in stone_dict:
            for j in stone_dict[stones[i] - d]:
                if i != j:
                    stone_pairs.add(tuple(sorted([i, j])))

    # 步骤3：将索引对的集合转换为包含实际石头重量的元组集合
    result = set()
    for pair in stone_pairs:
        weight_pair = tuple(sorted([stones[pair[0]], stones[pair[1]]]))
        result.add(weight_pair)

    return result


if __name__ == '__main__':

    #Question B.4和Question C测试
    for test_sample in test_samples:
        stones_weight=test_sample.stones_weights
        diff=test_sample.differ
        ans=test_sample.ans
        #Question B.4代码测试
        pred_ans=find_stone_pair(stones_weight,diff)
        if ans==pred_ans or (pred_ans is not None and abs(pred_ans[1]-pred_ans[0])==diff):
            print("找到的石头对是满足要求的")

        #Question C代码测试 测是
        pred_ans_all = find_stone_pairs(stones_weight, diff)
        print(pred_ans_all)


