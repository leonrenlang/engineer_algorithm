# 问题：给定一个整数数组  nums，求出数组从索引 i 到 j  (i ≤ j) 范围内元素的总和，
# 包含 i,  j 两点。


# 思路：为了让求arr[i:j+1]的复杂度降到1
# - 采用一个辅助dp，dp[i] = sum(arr[0] + arr[1] + ... + arr[i])
# - 则：arr[i:j+1] = dp[j] - dp[i-1]
class NumArray:
    def __init__(self, nums):
        self.arr = []
        for i in range(len(nums)):
            self.arr.append(self.arr[i] + nums[i])

    def sumRange(self, i: int, j: int) -> int:
        return self.arr[j] - self.arr[i - 1]
