

# 如果s中包含重复的子字符串，那么说明s中至少包含两个子字符串，
# s+s至少包含4个字串，前后各去掉一位，查找s是否在新构建的字符串中。
def process(s):
    return s in (s + s)[1:-1]


# 思想：
# - 遍历子串可能取得的长度[0, len(s)//2]
# - 如果子串长度能被整除，则由字串构造字符串与字符串进行比较
def process(s):
    n = len(s)
    asumpt_sublen = n // 2
    while asumpt_sublen >= 1:
        if n % asumpt_sublen != 0:
            asumpt_sublen -= 1
            continue
        else:
            if s[:asumpt_sublen] * (n // asumpt_sublen) == s:
                return True
            else:
                asumpt_sublen -= 1
    return False


if __name__ == '__main__':
    s = 'abcabcd'
    print(process(s))
