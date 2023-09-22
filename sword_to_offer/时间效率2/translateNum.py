    
# 把数字翻译成字符串
#给定一个数字，我们按照如下规则把它翻译为字符串：0 翻译成 “a” ，
# 1 翻译成 “b”，……，11 翻译成 “l”，……，25 翻译成 “z”。一个数字可能有多个翻译。
# 请编程实现一个函数，用来计算一个数字有多少种不同的翻译方法。

'''
思路1：
递归方程:f(i) = f(i+1) + g(i,i+1)*f(i+2)其中i代表当前下标,
g(i,i+1)代表了坐标i和i+1所指向的数字所组成的两位数,如果这个两位数在10到25之间那么g(i,i+1) = 1,
否则g(i,i+1) = 0
说明： 仍存在重复子问题，应采用自底向上的方法重写。
'''
class Solution(object):
    def translateNum(self, num):
        """
        :type num: int
        :rtype: int
        """
        def Count_sum(string, i, length):

            if i >= length:
                return 1    
            if i <= length -1:
                converted = int(string[i]) * 10 + int(string[i+1])

                if converted >= 10 and converted <= 25:             # 如果往后两位数在10<=x<=25的范围内，那么需要考虑f(i+2)
                    return Count_sum(string, i+1, length) + Count_sum(string, i+2, length)
                else:                                               # 否则只考虑f(i + 1)
                    return Count_sum(string, i+1, length)
        string = str(num)
        length = len(string) - 1
        return Count_sum(string, 0, length)

# 思路2：动态规划
# 搞清楚赋值顺序
class Solution:
    def translateNum(self, num: int) -> int:
        s, a, b = str(num), 1, 1
        for i in range(1, len(s)):
            '''
            # 两个赋值可以认为是并发的，互不影响, 等价于以下代码
            tmp = a
            a = b
            b = tmp + b if 10 <= int(s[i - 1:i + 1]) <= 25 else b
            '''
            a, b = b, ((a+b) if 10 <= int(s[i - 1:i + 1]) <= 25 else b)
        return b
