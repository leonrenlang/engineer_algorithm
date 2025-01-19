
""" 
题目1： 输入一个递增排序的数组和一个数字s，在数组中查找两个数，
使得它们的和正好是s。如果有多对数字的和等于s，则输出任意一对即可。


思路：
    两个指针向中间逼近
"""
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) < 2: return []
        first, last = 0, len(nums) - 1
        while first < last:
            sum_tmp = nums[first] + nums[last]
            if  sum_tmp < target:
                first += 1
            elif sum_tmp > target:
                last -= 1
            else:
                return [nums[first], nums[last]]

""" 
题目2：输入一个正整数 target ，输出所有和为 target 的连续正整数序列（至少含有两个数）。
序列内的数字由小到大排列，不同序列按照首个数字从小到大排列。
"""


class Solution(object):
    def findContinuousSequence(self, target):
        """
        :type target: int
        :rtype: List[List[int]]
        """
        if target <= 2:
            return []
        
        low, high, cur_sum = 1, 2, 3
        result = []
        while high <= target / 2 + 1:                   #最少两个数且连续
            if cur_sum == target:                              
                result.append([i for i in range(low, high+1)])
                high += 1
                cur_sum += high
            elif cur_sum < target:
                high += 1
                cur_sum += high
            else:
                cur_sum -= low
                low += 1
        return result
