# 问题：给一个数组arr,和一个整数aim，如果可以任意选择arr中的数字，能不能“刚好”累加得到aim
# 返回True or False


# dp[i][j]: 只准用前i的钱，目标为j，是否能够找零
# base case: 目标不为0， 但是无可选用零钱，返回False, 目标为0，不管有没有钱，都返回True
def make_change(arr, aim):
    N = len(arr) + 1
    dp = [[False] * (aim + 1) for _ in range(N + 1)]
    for i in range(N + 1):
        dp[i][0] = True
    for i in range(1, N + 1):
        for j in range(1, aim + 1):
            if j < arr[i - 1]:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j - arr[i - 1]] or dp[i - 1][j]
    return dp[N][aim]


# 问题2：分割等和子集问题:给定一个只包含正整数的非空数组arr,是否可以将这个数组分割成两个子集,使两个
# 子集的元素和相等


# 思想：
# - 这个问题可以转换成一个背包容量为sum(arr)/2, 和len(arr)个物品,是
# 否存在一种装法能“刚好装满”的问题（找零问题）
# 动态规划:
def fun(arr):
    summ = sum(arr)
    if not summ % 2 == 0: return False
    summ = summ // 2

    dp = [[False for _ in range(summ + 1)] for _ in range(len(arr) + 1)]
    for i in range(len(arr) + 1):
        dp[i][0] = True
    for i in range(1, len(arr) + 1):
        for w in range(1, summ + 1):
            if w < arr[i - 1]:
                dp[i][w] = dp[i - 1][w]
            else:
                dp[i][w] = dp[i - 1][w] or dp[i - 1][w - arr[i - 1]]
    return dp[-1][-1]
