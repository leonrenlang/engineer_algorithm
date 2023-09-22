# 问题： 给定一个目标金额，和一系列不同币值的硬币，各种币值的硬币可以重复使用
# 问共有多少种选择方式。


# 思路：
# - base case： dp[0][..] = 0 dp[..][0] = 1  dp[0][0] = 1
# - 转换方程的不同：
#             if j < arr[i - 1]:  # 当前的币种太大，没有办法继续使用了
#                 dp[i][j] = dp[i - 1][j]
#             else:  # 当前这个币种不用了，或者仍用当前这个币种
#                 dp[i][j] = dp[i - 1][j] + dp[i][j - arr[i - 1]]
# 当选择要当前的硬币，仍可继续选当前币值的硬币
# - 扩展：
# 什么不能使用dp[j] = sum(dp[j-coin] coin 属于 coins)，因为这样会让先选面值为1，再选面值为2
# 与先选面值为2，再选面值为1的情况变成两种情况，而实际上这是一种情况。
def make_change2(arr, target):
    '''
    arr:    硬币金额
    target: 目标金额
    '''
    N = len(arr)
    dp = [[0] * (target + 1) for _ in range(N + 1)]
    for i in range(N + 1):
        dp[i][0] = 1
    for i in range(1, N + 1):       # i代表第i个币种
        for j in range(1, target + 1):
            if j < arr[i - 1]:  # 当前的币种太大，没有办法继续使用了
                dp[i][j] = dp[i - 1][j]
            else:  # 当前这个币种不用了，或者仍用当前这个币种
                dp[i][j] = dp[i - 1][j] + dp[i][j - arr[i - 1]]
    return dp[N][target]


if __name__ == '__main__':
    arr = [1, 2, 5]
    target = 5
    print(make_change2(arr, target))
