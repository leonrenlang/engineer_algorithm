# 问题：在给定字符串前面可以添加字符使其成为回文串，
# 找到并返回可以用这种方式转化的最短回文串。


# 思想：
# - 找到从第一个字符开始的最长回文子串，然后将后面的子串
# 翻转放到原始字符串前面。
# - 找最长回文子串，将原字符串翻转，
def violence(s):
    if not s: return ''
    r = s[::-1]
    for i in range(len(s)):
        if s[:len(s) - i] == r[i:]:  # 将原字符串与翻转字符串逐一对比
            if i == 0:  # 如果字符串本身就是回文，则直接返回
                return s
            else:
                break
    return s[-i:][::-1] + s


s = "aba"
print(violence(s))
