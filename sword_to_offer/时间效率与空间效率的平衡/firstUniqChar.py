
# 第一个只出现一次的字符
# 在字符串 s 中找出第一个只出现一次的字符。如果没有，返回一个单空格。

class Solution:
    def firstUniqChar(self, s: str) -> str:
        dic = {}
        for c in s:
            dic[c] = not c in dic   # 如果c已经在dic中，设为0
        for c in s:
            if dic[c]: return c     # 找到第一个为1的dic
        return ' '

