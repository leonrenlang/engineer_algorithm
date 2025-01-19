
# 数组中出现次数超过一半的数字

# 思路1，摩尔投票法，目标数字的频次超过其他所有数字，可以用投票，最终剩下的肯定是目标数字
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if not nums: return None
        votes = 0
        res = 0
        for item in nums:
            if votes == 0:
                res = item
            if item == res:
                votes += 1
            else:
                votes -= 1
        return res

# 思路2，基于patition的方法，待补完
