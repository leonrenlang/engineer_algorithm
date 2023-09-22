
'''
题目1： 在一个数组 nums 中除一个数字只出现一次之外，其他数字都出现了三次。请找出那个只出现一次的数字。
'''
'''
我们想一下如果一个数字出现三次,那么他的二进制位表示的每一位(0或1)也出现了三次.
如果把所有出现三次的数字的二进制表示的每一位都分别加起来,那么每一位的和都能被3整除
我们把所有数字的二进制位的每一位加起来.若果某一位的和能被3整除,
那么那个只出现一次的数字二进制表示中对应的那一位为0,否则为1

步骤:
统计所有数字二进制位的和
判断每一位的和能否被3整除,求解最后结果
时间复杂度O(n),空间复杂度O(1)(常数空间))
'''

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        bitSum = [0] *32 #定义存储各个位的数组

        for i in nums: #统计各位之和
            mask = 1
            for j in reversed(range(32)):
                if mask & i:
                    bitSum[j] += 1
                mask = mask << 1

        result = 0
        for i in range(32):#得到最终结果
            result = result << 1
            result += bitSum[i] % 3

        return result



""" 
题目2：一个整型数组 nums 里除两个数字之外，其他数字都出现了两次。
请写程序找出这两个只出现一次的数字。
要求时间复杂度是O(n)，空间复杂度是O(1)。 
"""
""" 
思路：
将所有数字异或，找到结果第一位为1的值，根据数组中的数与该位异或的结果划分为两个数组
分别对两个数组异或，得到结果
 """

class Solution:
    def singleNumbers(self, nums):
        ret = 0  # 所有数字异或的结果
        
        for n in nums:
            ret ^= n

        # 找到第一位不是0的
        h = 1
        while(ret & h == 0):
            h <<= 1

        a = 0       #返回的第一个数字
        b = 0       #返回的第二个数字
        for n in nums:
            # 根据该位是否为0将其分为两组
            if (h & n == 0):
                a ^= n
            else:
                b ^= n

        return [a, b]
