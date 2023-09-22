# 问题：
# 将一串数字还原成字母编码的方式数
# 一条包含字母 A-Z 的消息通过以下方式进行了编码：
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
# 给定一个只包含数字的非空字符串，请计算解码方法的总数。
# 示例 1:
# 输入: "12"
# 输出: 2
# 解释: 它可以解码为 "AB"（1 2）或者 "L"（12）。

# 思想：
# - 如果只有一个数字 -> 只有一种解码方式
# - 如果有两个数字 -> 可能

# - 可以看做爬楼梯问题，s[:i]的解码方式数=s[:i-1]+s[:i-2]
# - 但要求s[i-1]不为0， s[i-1:i+1]可以解码
def fun(s):
    dp_i_2 = 1
    dp_i_1 = 1 if s[0] != '0' else 0
    for i in range(1, len(s)):
        cur = 0
        # 状态转移方程，如果s[i]!='0'，则它是一个1~9的普通数字，若考虑其和dp[i-1]的关系
        # 该字母只能单独编码，编码可能数并不会增加
        if s[i] != '0':
            cur += dp_i_1
        # 考虑dp[i]和dp[i-2]的关系,当前字母和前一个字母必须当做一个整体进行编码
        if '10' <= s[i - 1:i + 1] <= '26':
            cur += dp_i_2
        

        dp_i_2 = dp_i_1
        dp_i_1 = cur
    return dp_i_1


if __name__ == '__main__':
    string = '12'
    print(fun(string))
