#  把数组排成最小的数
# 输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。

# 思路1：利用字符串的比较
import functools
def compare(s1, s2):
    if s1+s2 < s2+s1:       #字符串的比较，一位一位的比较
        return -1
    elif s1+s2 == s2+s1:
        return 0
    else:
        return 1
class Solution(object):
    def minNumber(self, numbers):
        if not numbers: return ''
        if len(numbers) == 1: return str(numbers[0])
        str_numbers = [str(n) for n in numbers]
        return ''.join(sorted(str_numbers, key=functools.cmp_to_key(compare)))




