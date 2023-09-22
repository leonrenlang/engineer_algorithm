# --------------------------------------------------------------
# 问题5/6： k=2, k=n
# 状态转移方程：
# dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
# dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])
# base case:
def process(prices, k):
    if not prices: return 0
    if k > len(prices) / 2:  # 当k大于prices数组的一般，就相当于无限次数，写这个为了不被卡时间
        dp_i_0, dp_i_1 = 0, -float('inf')
        for price in prices:
            tmp = dp_i_0
            dp_i_0 = max(dp_i_0, dp_i_1 + price)
            dp_i_1 = max(dp_i_1, tmp - price)
        return dp_i_0

    dp = [[[0] * 2 for _ in range(k + 1)] for _ in range(len(prices))]
    for i in range(len(prices)):
        for k in range(1, k + 1):
            if i == 0:
                dp[i][k][0] = 0
                dp[i][k][1] = -prices[0]
            else:
                dp[i][k][0] = max(dp[i - 1][k][0], dp[i - 1][k][1] + prices[i])
                dp[i][k][1] = max(dp[i - 1][k][1], dp[i - 1][k - 1][0] - prices[i])
    return dp[-1][-1][0]


if __name__ == '__main__':
    arr = [3, 3, 5, 0, 0, 3, 1, 4]
    res = process(arr, 2)
    print(res)
