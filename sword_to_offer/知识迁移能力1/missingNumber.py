


#  0～n-1中缺失的数字
'''
一个长度为n-1的递增排序数组中的所有数字都是唯一的，并且每个数字都在范围0～n-1之内。
在范围0～n-1内的n个数字中有且只有一个数字不在该数组中，请找出这个数字。
'''
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total_num = len(nums)
        return int(total_num*(total_num + 1) // 2) - sum(nums)

class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        first, last = 0, len(nums) - 1
        while first <= last:
            mid = (first + last) // 2
            if nums[mid] == mid: first = mid + 1
            else: last = mid - 1

        return first        #最后last会在最后一个num[last] = last的值上，first = last + 1