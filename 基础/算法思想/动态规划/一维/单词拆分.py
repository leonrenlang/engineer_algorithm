# 问题：
# 给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，
# 判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。
# 示例
# 输入: s = "applepenapple", wordDict = ["apple", "pen"]
# 输出: true


# 思想：
# - 这个方法的巧妙之处在于不是大问题到小问题，而是解决每个小问题能够解决的大问题
# - 因为单词的长度不定，dp[i]之前dp[:i]的子问题是很难初始化的
def word_bread(s, wordDict):
    dp = [False] * (len(s) + 1)
    dp[0] = True
    for i in range(len(s)):
        if dp[i] == True:
            for j in range(i + 1, len(s) + 1):  # 注意j的范围非常tricky
                if s[i:j] in wordDict:
                    dp[j] = True
    return dp[-1]
