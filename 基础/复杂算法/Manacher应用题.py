# 问题：如果只能在字符串的最后添加字符，让字符串变成回文，如何让字符串的字符最少


# 思想：
# - 其实就是求必须包含最后一个字符的最长回文子串
# - 当最右回文边界第一次到达了最后一个字符，此时的中心就是我们要找的中心点
# 最后一个字符就是该中心点对应回文的有边界。


def func(s):
    s_pad = "#" + '#'.join(list(s)) + "#"
    n = len(s_pad)
    dp = [0] * n
    most_r = 0
    center = 0
    for i in range(1, n - 1):

        if i < most_r:
            i_mirror = 2 * center - i
            dp[i] = min(dp[i_mirror], most_r - i)
        while i + 1 + dp[i] <= n - 1 and \
                i - 1 - dp[i] >= 0 and \
                s_pad[i + 1 + dp[i]] == s_pad[i - 1 - dp[i]]:
            dp[i] += 1

        if i + dp[i] > most_r:
            center = i
            most_r = i + dp[i]

        if most_r >= n:
            max_contain_end = dp[i]
            break

    res = s[-max_contain_end:]
    return res


s = 'I am chinese'
print(func(s))
