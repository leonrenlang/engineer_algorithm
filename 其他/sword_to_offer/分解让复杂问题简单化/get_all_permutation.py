


# 输入一个字符串，打印出该字符串中字符的所有排列。
# 思路：取出第i个数，全排列其他非i位置的数拼在后面。
#       你可以以任意顺序返回这个字符串数组，但里面不能有重复元素。


class Solution(object):
    def permutation(self, ss):
        if not ss: return []
        words = list(ss)
        def helper(s):
            if len(s) == 1:
                return s[0]
            res = []
            for i in range(len(s)):
                l = helper(s[:i] + s[i+1:])
                for j in l:
                    res.append(s[i] + j)
            return res
        return list(sorted(set(helper(words))))

