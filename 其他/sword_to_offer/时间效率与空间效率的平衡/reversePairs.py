
# 数组中的逆序对
#在数组中的两个数字，如果前面一个数字大于后面的数字，
# 则这两个数字组成一个逆序对。
# 输入一个数组，求出这个数组中的逆序对的总数。


class Solution(object):
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        def Merge_sort(s):
            n = len(s)
            if n < 2:
                return
            mid = n // 2
            s1 = s[0:mid]
            s2 = s[mid:n]
            Merge_sort(s1)
            Merge_sort(s2)
            Merge(s1,s2,s)

        def Merge(s1,s2,s):
            len_s1 = len(s1) - 1
            len_s2 = len(s2) - 1
            temp = len(s) - 1
            
            while len_s1 >=0 and len_s2 >= 0:
                if s1[len_s1] > s2[len_s2]:
                    s[temp] = s1[len_s1]
                    result[0] += len_s2 + 1
                    len_s1 -= 1
                    temp -= 1
                else:
                    s[temp] = s2[len_s2]
                    len_s2 -= 1
                    temp -= 1
                    
            while len_s1 >= 0:
                s[temp] = s1[len_s1]
                len_s1 -= 1
                temp -= 1
            while len_s2 >= 0:
                s[temp] = s2[len_s2]
                temp -= 1
                len_s2 -= 1
        
        
        result = [0]
        Merge_sort(nums)
        return result[0]


