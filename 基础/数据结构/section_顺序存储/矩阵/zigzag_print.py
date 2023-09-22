
"""  
“之”字形打印矩阵
【题目】 给定一个矩阵matrix，按照“之”字形的方式打印这
个矩阵，例如： 1 2 3 4 5 6 7 8 9 10 11 12
“之”字形打印的结果为：1，2，5，9，6，3，4，7，10，11，
8，12
【要求】 额外空间复杂度为O(1)。
"""


# 思路：如果局部位置太恶心了，那一般有一个宏观思路
def print_level(matrix, a_row, a_col, b_row, b_col, from_up):
    if from_up:
        while a_row != b_row+1:
            print(matrix[a_row][a_col])
            a_row += 1
            a_col -= 1
    else:
        while b_row != a_row-1:
            print(matrix[b_row][b_col])
            b_row -= 1
            b_col += 1

def zigzag_print_matrix(matrix):
    a_row, a_col = 0, 0
    b_row, b_col = 0, 0
    rightdown_row, rightdown_col = len(matrix)-1, len(matrix[0])-1
    from_up = False
    while a_row <= rightdown_row:
        print_level(matrix, a_row, a_col, b_row, b_col, from_up)
        a_row = 0 if a_col != rightdown_col else a_row + 1
        a_col = a_col + 1 if a_col != rightdown_col else a_col
        b_col = 0 if b_row != rightdown_row else b_col + 1
        b_row = b_row + 1 if b_col == 0 else b_row
        from_up = not from_up
    
import numpy as np
array = np.random.randint(0,100,(3,10))
print(array)
zigzag_print_matrix(array)