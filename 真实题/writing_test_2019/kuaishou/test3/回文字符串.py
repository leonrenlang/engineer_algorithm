# 题目描述
# 最大回文子串是被研究得比较多的一个经典问题。最近月神想到了一个变种，对于一个字符串，
# 如果不要求子串连续，那么一个字符串的最大回文子串的最大长度是多少呢。

# 输入描述:
# 每个测试用例输入一行字符串（由数字0-9，字母a-z、A-Z构成），字条串长度大于0且不大于1000.
# 输出描述:
# 输出该字符串的最长回文子串的长度。（不要求输出最长回文串，并且子串不要求连续）

# 示例1
# 输入
# adbca
# 输出
# 3
# 示例2
# 输入
# abdfgbca
# 输出
# 5
# 说明
# 因为在本题中，不要求回文子串连续，故最长回文子串为aba(或ada、aca)
# 备注:
# 因为不要求子串连续，所以字符串abc的子串有a、b、c、ab、ac、bc、abc7个

# 思想：
# - 父问题与子问题的关系：假设字符串长度为n，如果首尾相等
# 那么f(n)等于去首尾的f(n-2)+2,否则等于max(f(n-1)去首，f(n-1)去尾）
# - base case所有的f(1)问题结果均为1
# - 用两个变量组成区间[i,j]，表示区间[i,j]中包含非连续最长回文字符串的长度
# 则可转换成需要一个辅助二维数组的动态规划问题


def process(string):
    dp = [[0 for _ in range(len(string))] for _ in range(len(string))]
    for i in range(len(string)):
        dp[i][i] = 1
    i = len(string) - 2
    while i >= 0:
        for j in range(i + 1, len(string)):
            if string[i] == string[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        i -= 1
    print(dp[0][len(string) - 1])


if __name__ == '__main__':
    string = input()
    process(string)
