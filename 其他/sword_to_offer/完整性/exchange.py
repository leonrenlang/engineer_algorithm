

# 调整数组顺序使奇数位于偶数前面
# 可以归类为将数组中的数分为两类的方法
class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        odd_idx = 0
        for i in range(0, len(nums)):
            if nums[i] % 2 == 0:
                continue
            else:
                nums[i], nums[odd_idx] = nums[odd_idx], nums[i]
                odd_idx += 1
        return nums