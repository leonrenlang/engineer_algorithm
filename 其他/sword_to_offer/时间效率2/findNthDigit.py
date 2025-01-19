

# 数字序列中某一位的数字
'''
数字以0123456789101112131415…的格式序列化到一个字符序列中。在这个序列中，第5位（从下标0开始计数）是5，第13位是1，第19位是4，等等。

请写一个函数，求任意第n位对应的数
'''


class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 9:
            return n

        m = 2               #找到当前的n所在的区间
        temp = 90
        n -= 9
        while n > m * temp:
            n -= m*temp
            m += 1
            temp *= 10

        temp1 = n % m               # 比如三位数区间，求余，知道是某数的第几个
        temp2 = n // m
        if temp2:#不是否为序列的第一个数字
            if n % m: #有余数
                return int(str(10**(m-1) + (n // m))[temp1-1])
            else:#没有余数
                return int(str(10**(m-1) + (n // m)-1)[temp1-1])
        else:#是第一个数字
            return int(str(10**(m-1))[temp1-1])
