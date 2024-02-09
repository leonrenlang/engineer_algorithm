# 问题：给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金
# 额所需的“最少的硬币个数”。如果没有任何一种硬币组合能组成总金额，返回 -1。

# 动态规划写法
# dp[i]代表组成金额i需要的最少硬币数量
def fun3(coins, amount):
    dp = [amount + 1] * (amount + 1)  # 初始值设置为-1为了判断是否能够找零
    dp[0] = 0
    for i in range(1, amount + 1):
        for coin in coins:
            if i < coin:  # 如果当前的金额小于硬币的面额，则跳过
                continue
            dp[i] = min(dp[i], dp[i - coin] + 1)
    return dp[-1] if dp[-1] != (amount + 1) else -1


# 递推公式：
# dp[i] = min(dp[i - coin])
# 递归写法
def fun2(coins, amount):
    def dp(n):
        if n == 0: return 0
        if n < 0: return -1
        res = float('INF')
        for coin in coins:
            tmp = dp(n - coin)
            if tmp == -1: continue
            res = min(res, 1 + tmp)
        return res if res != float('INF') else -1

    return dp(amount)


# 备忘录写法
def fun(coins, amount):
    memo = dict()

    def process(n):
        if n in memo: return memo[n]
        if n == 0: return 0
        if n < 0: return -1
        res = float('INF')
        for coin in coins:
            tmp = process(n - coin)
            if tmp == -1: continue
            res = min(res, tmp + 1)
        memo[n] = res if res != float('INF') else -1
        return memo[n]

    return process(amount)


if __name__ == '__main__':
    coins = [1, 2, 5]
    amount = 11
    print(fun3(coins, amount))
