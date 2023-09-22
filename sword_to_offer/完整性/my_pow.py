
# 实现幂函数
# 注意：1.x = 0, n为负数问题
# 使用快速求幂方法


class Solution:
    def myPow(self, x: float, n: int) -> float:

        if x == 0: return 0
        res = 1
        if n < 0: x, n = 1 / x, -n

        # 把n看作一个二进制数
        while n:
            if n & 1:
                res *= x
            x *= x
            n >>= 1
        return res