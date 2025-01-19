

# 圆圈中最后剩下的数字
# 总结递归公式

class Solution:
    def lastRemaining(self, n, m):
        res = 0
        for i in range(2, n+1):
            res = (res+m)%i
        return res
