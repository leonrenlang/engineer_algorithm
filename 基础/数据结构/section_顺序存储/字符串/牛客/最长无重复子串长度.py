# 思想：
# - 直觉上，使用动态规划，dp[i]代表以当前字符为结尾的最长
# 无重复子串长度，但是对于每个子问题，都要去和长度dp[i-1]的
# 字符比较，判断当前字符之前是出现过， 时间复杂度为O(n)
# - 用一个哈希表记录每个字符上一个出现的位置，则可避免上述过程
# 时间O(N), 空间O(N)

# 待补完
def process(arr):
    dp = [0] * len(arr)
    dp[0] = 1
    dic = {}
    for item in arr:
        dic[item] = -1

    for idx in range(1, len(arr) - 1):
        pass

if __name__ == '__main__':
    pass
