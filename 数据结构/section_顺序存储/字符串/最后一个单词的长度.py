# 给定一个仅包含大小写字母和空格 ' ' 的字符串 s，返回其最后一个单词的长度。如果字符串从左向右滚动显示，那么最后一个单词就是最后出现的单词。
# 如果不存在最后一个单词，请返回 0 。
# 说明：一个单词是指仅由字母组成、不包含任何空格字符的 最大子字符串。
# 示例:
# 输入: "Hello World"
# 输出: 5

def lengthOfLastWord(s):
    """
    :type s: str
    :rtype: int
    """
    if not s: return 0  # 考虑空字符串的情况
    idx = len(s) - 1
    while idx >= 0 and s[idx] == ' ':  # 考虑最后是空格或者全部是空格的情况
        idx -= 1
    if idx < 0: return 0
    count = 0
    for i in range(idx, -1, -1):
        if s[i] != ' ':
            count += 1
        else:
            break
    return count


if __name__ == '__main__':
    s1 = 'Hello  World'
    s2 = ''
    s3 = '   '
    s4 = 'hello'
    print(lengthOfLastWord(s4))
