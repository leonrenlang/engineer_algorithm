# 问题1: k = 1
# 由于新状态仅与相邻状态有关，因此只需要用两个变量保存状态即可，不用n*2的数组
def process(prices):
    import sys
    dp_i_0 = 0  # base case: 第-1天的情况
    dp_i_1 = -sys.maxsize
    for i in range(len(prices)):
        dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])  # 今天手上没有股票的情况
        dp_i_1 = max(dp_i_1, -prices[i])  # 今天手上有股票的情况
    return dp_i_0
