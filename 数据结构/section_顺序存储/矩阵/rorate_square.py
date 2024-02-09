"""
题目：给定一个整型正方形矩阵matrix，请把该矩阵调整成顺时针旋转90度的样子。
要求额外空间复杂度为O(1)。
"""


def rotate_clockwise(matrix):
    # 先按主对角线对称，再按y轴翻转
    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for idx in range(len(matrix)):
        matrix[idx] = matrix[idx][::-1]  # 这其实用了额外空间，可以自己写一个翻转


def rotate_anticlockwise(matrix):
    # 先按副对角线对称，再按y轴进行翻转
    n = len(matrix)
    for i in range(n):
        for j in range(n - i):
            matrix[i][j], matrix[n - 1 - j][n - 1 - i] = matrix[n - 1 - j][n - 1 - i], matrix[i][j]
    for idx in range(len(matrix)):
        matrix[idx] = matrix[idx][::-1]


def rotate_180(matrix):
    # 先按y轴翻转，再按y轴翻转
    # TODO ndarray按y轴翻转有点问题, ndarray的一维数组没法之间交换，而二维list可以
    for idx in range(len(matrix) // 2):
        matrix[idx], matrix[len(matrix) - 1 - idx] = matrix[len(matrix) - 1 - idx], matrix[idx]
    # for idx in range(len(matrix)):
    #     matrix[idx] = matrix[idx][::-1]


# ***思路2, 一个框一个框做，这个方法有点麻烦，但是可以应对顺时针，逆时针
def rotate_edge(matrix, tR, tC, dR, dC):
    times = dC - tC
    for i in range(times):
        matrix[tR][tC + i], matrix[tR + i][dC], matrix[dR][dC - i], matrix[dR - i][tC] = matrix[dR - i][tC], matrix[tR][
            tC + i], matrix[tR + i][dC], matrix[dR][dC - i]


def rotate(matrix):
    # square_type: list[[int]]
    tR, tC = 0, 0
    dR = len(matrix) - 1
    dC = len(matrix[0]) - 1
    while tR < dR:
        rotate_edge(matrix, tR, tC, dR, dC)
        tR, tC, dR, dC = tR + 1, tC + 1, dR - 1, dC - 1


if __name__ == '__main__':
    import numpy as np

    matrix = np.random.randint(1, 100, [4, 4])
    print(matrix)
    matrix = [list(row) for row in matrix]
    rotate_180(matrix)

    print(matrix)
