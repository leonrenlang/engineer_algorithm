# 问题：给定两个字符串 text1 和 text2，返回这两个字符串的最长公共子序列的长度。


# dp[i][j]:对于s1[1..i] s2[1..j]，他们的最长公共子序列长度是dp[i][j]
# 状态转移方程：
# if s1[i] == s2[j]: dp[i][j] = dp[i-1][j-1] + 1
# else: dp[i][j] = max(dp[i-1][j], dp[i][j-1])


def fun(s1, s2):
    if not s1 or not s2: return 0
    dp = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]
    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[-1][-1]
