
# 买卖股票一次最大获利

# 记录之前最低的价格

class Solution:
    def maxProfit(self, prices: list) -> int:
        if not prices: return 0
    
        min_before = prices[0]
        max_profit = 0
        for idx in range(1, len(prices)):
            if (prices[idx] - min_before) > max_profit:
                max_profit = prices[idx] - min_before

            if prices[idx] < min_before:
                min_before = prices[idx]

        return max_profit
            

