# 编写一个函数，以字符串作为输入，反转该字符串中的元音字母。
# 示例 1:
# 输入: "hello"
# 输出: "holle"
# 示例 2:
# 输入: "leetcode"
# 输出: "leotcede"


def reverse_vowels(s):
    if not s: return s
    left = 0
    right = len(s) - 1
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    s_lis = list(s)
    while left < right:
        if s_lis[left] in vowels and s_lis[right] in vowels:
            s_lis[left], s_lis[right] = s_lis[right], s_lis[left]
            left += 1
            right -= 1
        if s_lis[left] not in vowels:
            left += 1
        if s_lis[right] not in vowels:
            right -= 1
    return ''.join(s_lis)
