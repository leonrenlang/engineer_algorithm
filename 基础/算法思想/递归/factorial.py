# 我其实  不知道怎么算，但我知道怎么试
def factorial(n):
    if n == 1:  # base case（当样本量小到什么程度，我就不用划分子问题了）
        return 1
    return n * factorial(n - 1)

# 递归的要素：   1. base case  2. 父问题与子问题之间的关系

# 我知道怎么算
def factorial2(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res
