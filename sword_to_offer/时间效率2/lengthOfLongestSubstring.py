
# 最长不含重复字符的子字符串
# 请从字符串中找出一个最长的不包含重复字符的子字符串，计算该最长子字符串的长度。

# 思路：动态规划，分三种情况

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        dic = {}        # 用dict是因为同样的键，后一个会覆盖前一个
        max_length = 0
        cur_length = 0
        for i in range(len(s)):

            if s[i] not in dic or i - dic[s[i]] > cur_length:       #如果当前字符从未出现过，或者出现过，但是很久之前
                cur_length += 1 
            else:
                cur_length = i - dic[s[i]]                      # 否则的话，当前值就是与之前出现过的距离

            dic[s[i]] = i       #把每一个值存到字典中

            if max_length < cur_length:
                max_length = cur_length

        return max_length

# 同样的思路，使用数组存储中间结果
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s: return 0
        tmp = [1]
        dic = {s[0]:0}
        for i in range(1, len(s)):
            if s[i] not in dic or i - dic[s[i]] > tmp[-1]:
                tmp.append(tmp[-1] + 1)
            else:
                tmp.append(i - dic[s[i]])
            dic[s[i]] = i
        return max(tmp)

