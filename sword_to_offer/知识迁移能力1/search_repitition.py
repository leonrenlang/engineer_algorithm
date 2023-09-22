


# 统计一个数字在排序数组中出现的次数。
# 思路:用2分查找分别找到该数字左边和右边的数字的index,return right - left - 1

class Solution:
    def search(self, nums: [int], target: int) -> int:
        i, j = 0, len(nums) - 1
        while i <= j:                       # 判断条件一定要加等号，否则有可能会少判断一个数
            m = (i + j) // 2                
            if nums[m] <= target: i = m + 1         # 找目标的右边，所有这里加等号
            else: j = m - 1                         
        right = i                              #因为判断条件有等号，所以j会再往左移一位

        i, j = 0, len(nums) - 1
        while i <= j:               
            m = (i + j) // 2
            if nums[m] < target: i = m + 1
            else: j = m - 1
        left = j
        return right - left - 1

    
if __name__ == "__main__":
        
    nums = [5,7,7,8,8,10]
    target = 8
    s = Solution()
    print(s.search(nums, target))

    
