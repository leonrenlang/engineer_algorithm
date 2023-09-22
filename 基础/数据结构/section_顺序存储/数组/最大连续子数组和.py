# 问题：给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

# 示例:
# 输入: [-2,1,-3,4,-1,2,1,-5,4],
# 输出: 6
# 解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。

# 思想：动态规划，f(n）定义为以当前元素结尾的最大连续子数组和
# f(n) = max(f(n-1)+ai, ai)
def maxSubArray(nums):
    dp = [0] * len(nums)
    dp[0] = nums[0]
    for i in range(1, len(nums)):
        dp[i] = max(dp[i - 1] + nums[i], nums[i])
    return max(dp)


# 由于f(n)问题仅与f(n-1)问题有关，可仅用一个变量保存上一次的值，而不是建
# 立一个dp数组
def maxSubArray2(nums):
    last_num = nums[0]
    res = nums[0]
    for i in range(1, len(nums)):
        last_num = max(last_num + nums[i], nums[i])
        res = max(last_num, res)
    return res
