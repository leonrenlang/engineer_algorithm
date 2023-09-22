
# 连续子数组的最大和
# 以i结尾的数组的最大和为nums[i]
# 找最大即可

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[i] += max(nums[i-1], 0)
        return max[nums]


