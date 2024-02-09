# 问题：给定两个字符串，计算s1转换成s2的最小操作次数
# 可以进行如下三种操作：增、删、替换


# 思想1：递归：
# - 状态转移关系：用两个指针，分别指向两个字符串的尾部，指针之前为当前问题规模
# 若两个指针指向数值相同，则i-1, j-1；否则，当前问题的结果应该
# 是分别在当前指针上做增、删、替换三种操作结果的最小值。
# - base case:
# 当两个指针中的某一个指向空了，则只能将另一个字符串的数据删除，返回其剩余长度
def EditDistance(s1, s2):
    def process(s1, s2, i, j):
        if i == -1: return j + 1
        if j == -1: return i + 1
        if s1[i] == s2[j]:
            return process(s1, s2, i - 1, j - 1)
        else:
            return min(
                process(s1, s2, i, j - 1),  # 增
                process(s1, s2, i - 1, j),  # 删
                process(s1, s2, i - 1, j - 1)  # 改
            ) + 1
    return process(s1, s2, len(s1) - 1, len(s2) - 1)


# 思想2： 动态规划
# - 决定问题规模的可变状态有两个，分别对应两个字符串的长度，变化范围是[0, len(str1)], [0, len(str2)]
# 多一个是考虑字符串为空的情况, dp[i][j]代表将索引i之前的子字符串转换成索引j之前的子字符串需要的步骤数
# - base case: 某一个字符串为空，则代价为另一个字符串的长度
# - 转移方程：dp[i][j] =
# 1. 如果str1[i]==str2[j], 则dp[i][j] = dp[i-1][j-1]
# 2. 否则min(
def edit_distance(s1, s2):
    dp = [[0 for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]
    for i in range(1, len(s1) + 1):
        dp[i][0] = i
    for j in range(1, len(s2) + 1):
        dp[0][j] = j
    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(
                    dp[i - 1][j],  # 增
                    dp[i][j - 1],  # 减
                    dp[i - 1][j - 1]
                ) + 1
    return dp[-1][-1]


if __name__ == '__main__':
    s1 = 'chinese'
    s2 = '地址'
    print(edit_distance(s1, s2))
