"""
在行列都排好序的矩阵中找数
【题目】 给定一个有N*M的整型矩阵matrix和一个整数K，
matrix的每一行和每一 列都是排好序的。实现一个函数，判断K
是否在matrix中。 例如： 0 1 2 5 2 3 4 7 4
4 4 8 5 7 7 9 如果K为7，返回true；如果K为6，返
回false。
【要求】 时间复杂度为O(N+M)，额外空间复杂度为O(1)。
"""


# 思路：从第一行最右边的数开始往前找，大于目标值往左，小于目标值往下。
# 从左下开始找也可以，但是从左上或者右下找不行

def is_contain(matrix, num):
    row = 0
    col = len(matrix[0]) - 1
    while row < len(matrix) and col >= 0:
        if matrix[row][col] > num:
            col -= 1
        elif matrix[row][col] < num:
            row += 1
        else:
            return True
    return False


if __name__ == '__main__':
    import numpy as np

    matrix = np.array([[1, 2, 3], [4, 7, 9], [5, 10, 100]])
    print(matrix)
    print(is_contain(matrix, 6))
