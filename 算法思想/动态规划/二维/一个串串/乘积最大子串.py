# 问题：给你一个整数数组 nums ，请你找出数组中乘积最大的连续
# 子数组的乘积


# 算法思想：
# 状态：
# - dp[i][0]代表以第i个元素为结尾的乘积最大的连续子数组的乘积
# - dp[i][1]代表以第i个元素为结尾的乘积最小的连续子数组的乘积
# base case:
# - dp[0][0] = nums[0]
# - dp[0][1] = nums[0]
# 转移方程：
# dp[i][0] = max(dp[i-1][0]*nums[i], dp[i-1][1]*nums[i], nums[i])
# dp[i][1] = max(dp[i-1][0]*nums[i], dp[i-1][1]*nums[i], nums[i])


def max_product(nums):
    if not nums: return 0
    dp = [[0] * 2 for _ in range(len(nums))]
    dp[0][0], dp[0][1] = nums[0], nums[0]
    res = nums[0]
    for i in range(1, len(nums)):
        tmp1 = nums[i] * dp[i - 1][0]
        tmp2 = nums[i] * dp[i - 1][1]
        dp[i][0] = max(tmp1, tmp2, nums[i])
        dp[i][1] = min(tmp1, tmp2, nums[i])
        res = max(dp[i][0], res)
    return res

