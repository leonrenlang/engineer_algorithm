# 问题：给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）使得它们的和等于 n。
# # 你需要让组成和的完全平方数的个数最少。


# 思想
# 首先考虑组成n中的一个平方数，该平方数必须小于n，遍历所有可能的平方数，n-该平方数为剩下的问题规模
# 找到这些所有可能中的最小值即为n的解

# - 设定dp[i]为组成和为i的最少完全平方数的个数
# - dp[i] = min(dp[i - k * k] + 1)
# 时间复杂度：O(n*sqrt(n))  空间复杂度O(n)


def numSquares2(n):
    dp = [0] * n
    for i in list(range(n)):
        dp[i] = i + 1
        j = 1
        while i+1 - j*j >= 0:
            dp[i] = min(dp[i], dp[i-j*j] + 1)
            j += 1
    return dp[n-1]


def numSquares1(n):
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        dp[i] = i
        j = 1
        while i - j * j >= 0:  # 注意可以取等于号
            dp[i] = min(dp[i], dp[i - j * j] + 1)
            j += 1
    return dp[n]
