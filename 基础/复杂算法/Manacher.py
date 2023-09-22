# 问题：给定一个字符串中，找到最大回文子串


# 暴力法：
# - 遍历每一个元素，首先判断这个元素相邻的元素是否相等，如果相等，
# 当前回文长度+2，继续往外判断相邻元素。但是这种方法对于长度位偶数的字符串的处理有问题
# - 解决办法，使用某个符号进行填充，分别求每个字符为中心的最长回文串长度，包括
# 填充的字符
# - 时间复杂度是O(n2)

# 举例：11311  先处理成#1#1#3#1#1#
# - 字符串长度变成11，对于每个字符，分别看以其为中心的最长回文串的长度为多少
#  得到数字[1,3,5,3,1,11,1,3,5,3,1]
# - 最大的除以2，即为结果


# Manacher算法:
# - 首先建立一些概念：
# - 回文半径，每个元素为中心能找到的最长子串的半径长度
# 回文半径数组，每个元素的回文半径组成的数组
# - 最右回文右边界，从左往右依次遍历每个元素，每个元素的为中心的
# 最长子串的最右元素为其右边界；随着遍历，最右回文有边界也会跟着
# 更新，有可能前一个字符对应的右边界比当前字符的右边界还靠右，就不更新。
# - 回文右边界对应的中心，记录最右回文右边界的同时，需要记录其中心。
# 举例：1213121
# 回文半径数组：


# 思想：
# - 如果当前元素最右回文右边界外面，暴力
# - 如果没在外面，分为3中情况，设当前元素索引为i,i与最长回文右边界对应中心的对称点为i'
# 1. i'回文范围在（L, R)内，(L,R)指的是当前最右回文有边界和其对应的左边界。则当前元素i的回文半径等于i'的回文半径
# 2. i'回文范围超出了（L，R)， 则当前元素i的回文半径为i到右边界的距离
# 3. i'回文范围刚好与L重合，则当前元素i的回文半径为i到右边界的距离+继续往外扩。
# 时间复杂度：O(n), 只要在往外扩操作一定会使R增加，因此，时间复杂度不会超过O(n)


def longestPalindrome(s: str) -> str:
    s_pad = '#' + '#'.join(list(s)) + '#'
    n = len(s_pad)
    dp = [0] * n
    center, most_r = 0, 0
    for idx in range(1, n - 1):
        i_mirror = 2 * center - idx  # i'所在位置
        if idx < most_r:  # 在范围内，如果i'的范围没超出most_r,则dp[i] = dp[i_mirror]
            # 如果超过了，则结果为most_r-idx
            # 如果重合，则需要继续括
            dp[idx] = min(dp[i_mirror], most_r - idx)  # 先假设其值等于前两者中较小的，然后往外扩，就可以cover以上全部三种情况
        while (idx + 1 + dp[idx] < n and  # 并且能将i没在most_r范围，直接往外扩的情况考虑进去。
               idx - 1 - dp[idx] >= 0 and
               s_pad[idx + 1 + dp[idx]] == s_pad[idx - 1 - dp[idx]]):
            dp[idx] += 1

        if idx + dp[idx] > most_r:  # 更新most_r
            center = idx
            most_r = idx + dp[idx]
    idx = dp.index(max(dp))  # 找到最长回文子串的中心元素的索引
    start = (idx - dp[idx]) // 2  # 找到其起始位置
    return s[start: start + dp[idx]]  # 返回最长回文子串


def longestPalindrome(s: str) -> str:
    if s == "": return ""
    s1 = '$#' + '#'.join(s) + '#@'  # 加上外面两个字符是为了在下面简写while的条件
    mr = 0  # 已遍历的最大右边界
    mid = 0  # 对应的中心点
    n = len(s1)
    dp = [0] * n
    for i in range(1, n - 1):
        if i < mr:  # 可以利用之前保存的值
            dp[i] = min(mr - i, dp[mid * 2 - i])  # 不能超过已遍历的右边界
        t = 0
        while 1:  # 继续扩张
            if s1[i + dp[i] + t] != s1[i - dp[i] - t]:
                break
            t += 1
        dp[i] += t - 1
        if i + dp[i] > mr:  # 更新边界值
            mr = i + dp[i]
            mid = i
    maxlen, maxidx = 0, 0
    for i in range(n):  # 找最大子串
        if dp[i] > maxlen:
            maxlen = dp[i]
            maxidx = i
    return s1[maxidx - maxlen:maxidx + maxlen + 1].replace('#', "")


string = 'I am chinese'
print(longestPalindrome(string))
