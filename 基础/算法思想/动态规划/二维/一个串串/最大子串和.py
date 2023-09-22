# 问题：给定一个整数数组，找出总和最大的连续数列，并返回总和。

# 说明：字串必须遍历，子序列可以不连续

# 思想：动态规划
def maxSubArray(nums):
    dp = [0] * len(nums)
    dp[0] = nums[0]
    for i in range(1, len(nums)):
        dp[i] = dp[i - 1] + nums[i] if dp[i - 1] > 0 else nums[i]
    return max(dp)


if __name__ == '__main__':
    nums = [-2, 1, -3, 4, -1, 2, 2, -5, 4]




