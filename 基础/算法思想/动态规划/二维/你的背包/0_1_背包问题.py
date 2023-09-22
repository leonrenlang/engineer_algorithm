# 问题：
# 给一个重量W和N个物品，每个物品有重量和价值两个属性。
# 请问用这个背包装物品，“最多能装”的价值是多少？


# 思想：动态规划
# - 有两个可变状态：背包的容量[0,W]，可用的物品[0,len(goods)],
# dp[W, i]代表可用背包容量为W,可选物品为i之前的所有物品时可装的最大价值
# - base case: dp[0][..] = 0, dp[..][0] = 0, 无背包容量，无可选物品，可装价值均为0
# - 转移方程:
#      dp[i][w] = max(
#                     dp[i - 1][w],
#                     dp[i - 1][w - goods[i][0]] + goods[i][1]
#                   )
def knapsack(W, goods):
    N = len(goods)
    dp = [[0] * (W + 1) for _ in range(N + 1)]
    for i in range(1, N + 1):
        for j in range(1, W + 1):
            if j < goods[i - 1][0]:  # 注意，这里要用i-1
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - goods[i - 1][0]] + goods[i - 1][1])
    return dp[N][W]


# 思想：递归
# 递归关系：对于每件物品，只能选择放进背包和不放进背包，但是当背包的容量不够时，只能选择放
# base case： 没有物品要放了，直接返回0
def knapsack2(W, goods):
    def process(W, goods, i):
        if i == len(goods):
            return 0
        if W < goods[i][0]:
            return process(W, goods, i + 1)
        else:
            return max(process(W - goods[i][0], goods, i + 1) + goods[i][1], process(W, goods, i + 1))

    res = process(W, goods, 0)
    return res


if __name__ == '__main__':
    goods = [(1, 2), (3, 4), (5, 6)]  # goods[0][0]是第一件物品的重量，goods[0][1]是第一件物品的价值
    W = 10
    res = knapsack(W, goods)
    res2 = knapsack(W, goods)
    print(res)
    print(res2)
