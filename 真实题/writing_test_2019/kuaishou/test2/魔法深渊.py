# 问题：已知深渊有N层台阶构成（1 <= N <= 1000)，并且每次月神仅可往上爬2的整数次幂个台阶(1、2、4、....)，
# 请你编程告诉月神，月神有多少种方法爬出深渊

# 输入描述:
# 输入共有M行，(1<=M<=1000)
# 第一行输入一个数M表示有多少组测试数据，
# 接着有M行，每一行都输入一个N表示深渊的台阶数

# 输出描述:
# 输出可能的爬出深渊的方式

# 示例1
# 输入
# 4
# 1
# 2
# 3
# 4
# 输出
# 1
# 2
# 3
# 6
# 备注:
# 为了防止溢出，可将输出对10^9 + 3取模

# 思路：动态规划
# - dp[n] = dp[n-1] + dp[n-2] + dp[n-4] ...
# - base case: n=0 -> 1; n=1 -> 1。
def process(steps):
    _max = max(steps)  # 算到要求的最大台阶数即可
    dp = [0] * 1001
    dp[0] = 1
    MOD = pow(10, 9) + 3
    for i in range(1, _max + 1):
        t = 1
        while t <= i:
            dp[i] += dp[i - t]
            dp[i] %= MOD
            t *= 2
    for step in steps:
        print(dp[step])


if __name__ == '__main__':
    n = int(input())
    steps = []
    for _ in range(n):
        steps.append(int(input()))
    process(steps)  # 之所以不一个一个算，是因为存在重复计算
