



# 问题4：k = +infinity with fee
# 每次交易需要支付手续费，只需要在获取利润的时候，减去手续费即可
# dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
# dp[i][1] = max(dp[i-1][1], dp[i-1]-prices[i]-fee)
def process4(prices, fee):
    import sys
    dp_i_0 = 0  # 这里是i = -1时的base case
    dp_i_1 = -sys.maxsize
    for i in range(len(prices)):
        tmp = dp_i_0
        dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
        dp_i_1 = max(dp_i_1, tmp - prices[i] - fee)
    return dp_i_0
