# 给定一个字符串s和一个字符模式p，
# 实现支持‘.’ ‘*’ 的正则表达式匹配

def isMatch(text, pattern) -> bool:
    memo = dict()  # 备忘录

    def dp(i, j):
        if (i, j) in memo: return memo[(i, j)]
        if j == len(pattern): return i == len(text)

        first = i < len(text) and pattern[j] in {text[i], '.'}

        if j <= len(pattern) - 2 and pattern[j + 1] == '*':
            ans = dp(i, j + 2) or \
                  first and dp(i + 1, j)
        else:
            ans = first and dp(i + 1, j + 1)

        memo[(i, j)] = ans
        return ans

    return dp(0, 0)


# -----------------------过程------------------------------------


# 两个字符串匹配
def is_match(text, pattern):
    if not pattern: return not bool(text)
    first_match = bool(text) and pattern[0] == text[0]
    return first_match and isMatch(text[1:], pattern[1:])


# 处理通配符‘.’
def is_match(text, pattern):
    if not pattern: return not bool(text)
    first_match = bool(text) and pattern[0] in {text[0], '.'}
    return first_match and isMatch(text[1:], pattern[1:])


# 处理通配符‘*’
# 说明：
# - 当遇到 * 的时候，其可以是前面的字符重复0次或者重复无限次
# - 如果重复0次，相当于保留text，把前面的字符与 * 一起删掉，即为is_match(text, pattern[2:]
# - 否则，直接把pattern丢给子问题去解决，text在前面的匹配消耗掉1个字符，patter可以无限重复
# 不消耗字符，当text为0的时候，一定会退出，因此不必担心无限循环的问题
def isMatch(text, pattern):
    if not pattern: return not bool(text)

    # 这里很trick，当text没了，pattern还有，不是直接返回False,而是保留在first_match中，留之后判断
    # 因为如果出现text没了,pattern还剩*，应该返回True
    first_match = bool(text) and pattern[0] in {text[0], '.'}
    # 不判断长度索引可能会越界
    if len(pattern) >= 2 and pattern[1] == '*':
        return isMatch(text, pattern[2:]) or \
               first_match and isMatch(text[1:], pattern)
    else:
        return first_match and isMatch(text[1:], pattern[1:])


# 用备忘录优化
def isMatch(text, pattern) -> bool:
    memo = dict()  # 备忘录
    def process(i, j):
        if (i, j) in memo: return memo[(i, j)]
        if j == len(pattern): return i == len(text)
        first = i < len(text) and pattern[j] in {text[i], '.'}
        if j <= len(pattern) - 2 and pattern[j + 1] == '*':
            ans = process(i, j + 2) or \
                  first and process(i + 1, j)
        else:
            ans = first and process(i + 1, j + 1)
        memo[(i, j)] = ans
        return ans
    return process(0, 0)



if __name__ == '__main__':
    s1 = 'aab'
    s2 = 'c*a*b'
    print(isMatch(s1, s2))
