


# 问题3：k = +infinity with cool down
# 每次sell之后要等一天才能继续交易
# dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i])
# dp[i][1] = max(dp[i-1][1], dp[i-2][0]-prices[i])
def process3(prices):
    import sys
    dp_i_0 = 0
    dp_i_1 = -sys.maxsize - 1
    dp_pre_0 = 0  # 代表dp[i-2][0]
    for i in range(len(prices)):
        tmp = dp_i_0
        dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
        dp_i_1 = max(dp_i_1, dp_pre_0 - prices[i])  # 今天手上有，可能是昨天剩下的，也可能是前天没持有今天购买了
        dp_pre_0 = tmp
    return dp_i_0
