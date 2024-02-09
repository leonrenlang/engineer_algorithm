"""
转圈打印矩阵
【题目】 给定一个整型矩阵matrix，请按照转圈的方式打印它。
例如： 1 2 3 4 5 6 7 8 9 10 11 12 13 14
15 16 打印结果为：1，2，3，4，8，12，16，15，14，13，9，
5，6，7，11， 10
【要求】 额外空间复杂度为O(1)。
"""


def print_edge(matrix, leftup_row, leftup_col, rightdown_row, rightdown_col):
    if leftup_row == rightdown_row:
        idx = leftup_col
        while idx <= rightdown_col:
            print(str(matrix[leftup_row][idx]) + ' ')
            idx += 1
    elif leftup_col == rightdown_col:
        idx = leftup_row
        while idx <= rightdown_row:
            print(str(matrix[idx][leftup_col]) + ' ')
            idx += 1
    else:
        cur_col = leftup_col
        cur_row = leftup_row
        while cur_col != rightdown_col:
            print(str(matrix[cur_row][cur_col]) + ' ')
            cur_col += 1
        while cur_row != rightdown_row:
            print(str(matrix[cur_row][cur_col]) + ' ')
            cur_row += 1
        while cur_col != leftup_col:
            print(str(matrix[cur_row][cur_col]) + ' ')
            cur_col -= 1
        while cur_row != leftup_row:
            print(str(matrix[cur_row][cur_col]) + ' ')
            cur_row -= 1


def rotate_print_matrix(matrix):
    # 一次打印一圈
    leftup_row, leftup_col = 0, 0
    rightdown_row, rightdown_col = len(matrix) - 1, len(matrix[0]) - 1
    while leftup_row <= rightdown_row and leftup_col <= rightdown_col:
        print_edge(matrix, leftup_row, leftup_col, rightdown_row, rightdown_col)
        leftup_row, leftup_col = leftup_row + 1, leftup_col + 1
        rightdown_row, rightdown_col = rightdown_row - 1, rightdown_col - 1


if __name__ == '__main__':
    import numpy as np

    matrix = np.random.randint(1, 100, [5, 5])
    rotate_print_matrix(matrix)
