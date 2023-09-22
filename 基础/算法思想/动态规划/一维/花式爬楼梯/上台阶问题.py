# 问题：有个小孩正在上楼梯，楼梯有n阶台阶，小孩一次可以上1阶、2阶或3阶。
# 计算小孩有多少种上楼梯的方式。结果可能很大，你需要对结果模1000000007。


# 思想： 很简单的状态转移方程 dp[n] = dp[n-1] + dp[n-2] + dp[n-3]
# 确定几个最简单状态的结果就行

def waysToStep(n: int) -> int:
    if n <= 2: return n
    dp = [0] * n
    dp[0], dp[1], dp[2] = 1, 2, 4
    for i in range(3, n):
        dp[i] = (dp[i - 1] + dp[i - 2] + dp[i - 3]) % 1000000007
    return dp[n - 1]


print(waysToStep(3))