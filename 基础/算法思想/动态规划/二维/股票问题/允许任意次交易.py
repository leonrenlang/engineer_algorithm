



# 问题2： k = +infinity
# dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i])
# dp[i][1] = max(dp[i-1][1], dp[i-1][0]-prices[i])
# 状态转移方程：
# dp[i][1][0] = max(dp[i-1][+infinity][0], dp[i-1][+infinity][1] + prices[i])
# dp[i][1][1] = max(dp[i-1][+infinity][1], dp[i-1][+infinity][0] - prices[i])
# 观察公式可知，k都是+infinity，不会改变，因此k对状态转移没有影响了
# 可以直接去掉，可得：
# dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
# dp[i][1] = max(dp[i-1][1], dp[i-1]-prices[i])
# base case:
# dp[0][0] = max(dp[-1][0], dp[-1][1] + prices[i]) = max(0, -infinity+prices[0]) = 0
# dp[0][1] = max(dp[-1][1], dp[-1][0] - prices[i]) = max(-infinity, 0 - prices[0]) = -prices[0]
def process2(prices):
    import sys
    dp_i_0 = 0  # 这里是i = -1时的base case
    dp_i_1 = -sys.maxsize - 1
    for i in range(len(prices)):
        tmp = dp_i_0
        dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
        dp_i_1 = max(dp_i_1, tmp - prices[i])
    return dp_i_0

