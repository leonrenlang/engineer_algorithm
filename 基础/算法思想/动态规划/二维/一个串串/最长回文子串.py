# 问题：返回字符串的任意一个最长回文子串（子串一定是连续的）


# 思路：
# - dp[i][j]代表string[i,j]是否是一个回文，dp[i][j] == dp[i+1][j-1] and string[i][j]
# - base case: dp[i][i] 均为True
# - 需要额外考虑的问题： 如何输出结果？在进行dp的过程中，如果得到某个元素为True
# 则将其与ans做比较，注意如果字符串存在,ans内元素个数最少为1
def longest_palindrome(string):
    if not string: return ''
    n = len(string)
    dp = [[True] * n for _ in range(n)]
    ans = string[0]  # 注意： 必须这样初始化，因为如果string长度为1，进不了循环， 也因此需要加上if not string: return ''
    for i in range(n - 2, -1, -1):  # 由于dp[i][j]问题可能依赖于其左下角的问题，因此也需要从下往上进行遍历
        for j in range(i + 1, n):
            if string[i] == string[j]:
                dp[i][j] = dp[i + 1][j - 1]
            else:
                dp[i][j] = False
            if dp[i][j] and (j - i + 1) > len(ans):
                ans = string[i:j + 1]
    return ans




if __name__ == '__main__':
    string = 'a'
    print(longest_palindrome(string))
