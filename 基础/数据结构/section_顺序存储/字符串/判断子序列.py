# 问题：给定字符串 s 和 t ，判断 s 是否为 t 的子序列。
# 你可以认为 s 和 t 中仅包含英文小写字母。字符串 t 可能会很长（长度 ~= 500,000），
# 而 s 是个短字符串（长度 <=100）。

# 示例 1:
# s = "abc", t = "ahbgdc"
# 返回 true.


def func(s1, s2):
    # 两个指针分别指向两个字符串，如果两个字符串的值相同，则都加，如果不同，则长的加，
    idx1, idx2 = 0, 0
    while idx1 < len(s1) and idx2 < len(s2):
        if s1[idx1] == s2[idx2]:
            idx1 += 1
            idx2 += 1
        else:
            idx2 += 1
    return idx1 == len(s1)
