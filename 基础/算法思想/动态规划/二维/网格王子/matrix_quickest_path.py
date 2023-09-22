# 问题：给一个每个元素都是正数的二维数组，从左上角走到右下角，每一步只能向右或者向下
# 求沿途累加和的最小值。


# 思想：对于每个点，其到右下角的最小累加和是其值与右边和左边最小累加和中较小之和
# （当元素位于最后一行，最后一列的，行动收到限制）
def quickest_path(matrix):
    def process(matrix, i, j):
        if i == (len(matrix) - 1) and (j == len(matrix[0]) - 1):
            return matrix[i][j]
        if i == len(matrix) - 1:
            return matrix[i][j] + process(matrix, i, j + 1)
        elif j == len(matrix[0]) - 1:
            return matrix[i][j] + process(matrix, i + 1, j)
        else:
            return matrix[i][j] + min(process(matrix, i + 1, j), process(matrix, i, j + 1))

    res = process(matrix, 0, 0)
    return res


# 改动态规划：
# 这个问题的所有子问题都可以用参数i, j固定，而i, j的变化范围是一个矩阵。

def quickest_path2(matrix):
    # 这是从右下角走到左上角路径的版本
    dp = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    dp[0][0] = matrix[0][0]
    for i in range(1, len(matrix)):
        dp[i][0] = matrix[i][0] + dp[i - 1][0]
    for i in range(1, len(matrix[0])):
        dp[0][i] = matrix[0][i] + dp[0][i - 1]
    for i in range(1, len(matrix[0])):
        for j in range(1, len(matrix)):
            dp[i][j] = matrix[i][j] + min(dp[i - 1][j], dp[i][j - 1])
    return dp[-1][-1]


if __name__ == '__main__':
    import numpy as np

    matrix = np.random.randint(0, 10, (3, 3))
    print(matrix)
    res = quickest_path2(matrix)
    print(res)
