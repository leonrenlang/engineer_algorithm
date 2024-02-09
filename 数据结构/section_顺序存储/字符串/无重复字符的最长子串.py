# 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
# 示例 1:
# 输入: "abcabcbb"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
# 示例 2:
# 输入: "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
# 示例 3:
# 输入: "pwwkew"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
#      请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。


# 思想： 动态规划
# - dp[i]代表以当前元素为结尾的无重复字符的最长字串
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """

        :type s: str
        :rtype: int
        """
        dp = [1] * len(s)
        for i in range(1, len(s)):
            idx = i - dp[i - 1]
            for j in range(i - dp[i - 1], i):
                if s[i] == s[j]:
                    idx = j + 1
            dp[i] = (i - idx) + 1
        return max(dp)


# 思想：滑动窗口
# - 时间复杂度O(n),空间复杂度O(n)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        left = 0
        lookup = set()
        max_len = 0
        cur_len = 0
        for i in range(len(s)):
            cur_len += 1
            while s[i] in lookup:
                lookup.remove(s[left])
                left += 1
                cur_len -= 1
            if cur_len > max_len:   max_len = cur_len
            lookup.add(s[i])
        return max_len


if __name__ == '__main__':
    res = Solution().lengthOfLongestSubstring("abcabcbb")
    print(res)
