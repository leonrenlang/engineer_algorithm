# 问题：
# 有n个气球，编号0到n-1,每个气球上都标有一个数字
# 每当戳破一个气球i时，可以获得nums[left] * nums[i] * nums[right]个硬币
# 求能获得的硬币的最大数量


# 动态规划
# - 定义dp[i][j]为开区间（i,j)之间的的最优解，i, j 的范围均为[0, n+1], 原数组的首尾均填充了一个1
# - base case: dp[i][j] = 0 if j - i <= 1
# - 转移方程：dp[i][j] = max(dp[i][k] + dp[k][j] + nums[k]*dp[i]*dp[j]) for k in range(i+1, j)
# - 一个需要额外考虑的问题
def fun(nums):
    N = len(nums)  # 这句和下一句顺序别搞错了
    nums = [1] + nums + [1]
    dp = [[0] * (N + 2) for _ in range(N + 2)]  # base case，如果字符串长度小于等于0，结果为0
    for i in range(N, -1, -1):  # 为什么dp顺序要这样写？观察dp矩阵可以发现每个父问题要求其同行与同列子问题的解
        for j in range(i + 1, N + 2):
            for k in range(i + 1, j):
                dp[i][j] = max(dp[i][j], dp[i][k] + dp[k][j] + nums[k] * nums[i] * nums[j])

    return dp[0][N + 1]


if __name__ == '__main__':
    nums = [3, 1, 5, 8]
    print(fun(nums))
