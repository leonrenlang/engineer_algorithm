# 在6*9的方格中，以左上角为起点，右下角为终点，每次
# 只能向下走或者向右走，请问一共右多少种不同的走法。


# 思想：
# - 一共要走的步数为(n+m-2) = 13
# - 结果为C(13, 5) 或者C(13, 8)
def math(n, m):
    a = m - 1  # 横向要走的步数
    b = (n + m) - 2  # 一共要走的步数
    res = 1
    for i in range(b, b - a, -1):
        res *= i
    for i in range(1, a + 1):
        res //= i
    return res


# 动态规划
def process(n, m):
    dp = [[0] * m for _ in range(n)]
    for i in range(1, m):
        dp[0][i] = 1
    for i in range(1, n):
        dp[i][0] = 1

    for i in range(1, n):
        for j in range(1, m):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    print(dp)
    return dp[-1][-1]


n = 6
m = 9
print(math(n, m))
print(process(n, m))


def factorial(n):
    res = 1
    for item in range(1, n+1):
        res *= item
    return res