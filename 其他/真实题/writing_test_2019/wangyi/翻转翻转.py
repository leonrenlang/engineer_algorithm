# 问题: 给定N*M的矩阵，矩阵内所有元素牌面朝上，依次翻转矩阵内每张牌及其邻域（九宫格）
# 问最后有几张牌正面朝下

# 模式：这是一道找规律的题，给定了明确的计算步骤，直接暴力不可能满足时间要求


# 思想：画图可知，矩阵的边框元素本身加上邻域元素总个数均为偶数，内部元素本身加上邻域元素总个数均为奇数
# 翻转偶数次不变，翻转奇数次则正面朝下
def process2(n, m):
    if n == 1 and m == 1:
        return 1
    elif n == 1:
        return m - 2
    elif m == 1:
        return n - 2
    else:
        return (n - 2) * (m - 2)


# 思想：暴力方法，建立所述矩阵，依次进行所述操作，统计正面朝下个数
def process1(n, m):
    def update(matrix, i, j):
        for row in range(i - 1, i + 2):
            for col in range(j - 1, j + 2):
                if 0 <= row < len(matrix) and 0 <= col < len(matrix[0]):
                    matrix[row][col] = int(not matrix[row][col])

    matrix = [[1 for _ in range(m)] for _ in range(n)]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            update(matrix, i, j)
    res = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                res += 1
    return res


def main():
    '''
    input:
    输入的第一行为测试用例数t(1 <= t <= 100000),
    接下来t行，每行包含两个整数N,M(1 <= N, M <= 1,000,000,000)
    output:
    对于每个用例输出包含一行，输出牌面向下的块的个数
    example:
        input:
        5
        1 1
        1 2
        3 1
        4 1
        2 2
        output:
        1
        0
        1
        2
        0
    '''
    num_instance = int(input())
    for _ in range(num_instance):
        n, m = [int(item) for item in input().strip().split()]
        print(process2(n, m))


if __name__ == '__main__':
    main()
