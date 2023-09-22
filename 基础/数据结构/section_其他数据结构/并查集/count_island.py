

"""  
一个矩阵中只有0和1两种值，每个位置都可以和自己的上、下、左、右
四个位置相连，如果有一片1连在一起，这个部分叫做一个岛，求一个
矩阵中有多少个岛？
举例：
0 0 1 0 1 0
1 1 1 0 1 0
1 0 0 1 0 0
0 0 0 0 0 0
这个矩阵中有三个岛。
"""

# 思路：遍历每个元素，如果元素为1，count++，并且将该元素一个岛的感染为2。
def infect(matrix, i, j):
    n = len(matrix)
    m = len(matrix[0])
    if i<0 or i>=n or j<0 or j>=m or matrix[i][j] != 1:
        return 
    matrix[i][j] = 2
    infect(matrix, i-1, j)
    infect(matrix, i+1, j)
    infect(matrix, i, j+1)
    infect(matrix, i, j-1)
    
def infect2(matrix, i, j):
    # 传染并且返回这个岛的数字个数
    n = len(matrix)
    m = len(matrix[0])
    if i<0 or i>=n or j<0 or j>=m or matrix[i][j] != 1:
        return 0
    matrix[i][j] = 2
    l = infect2(matrix, i-1, j)
    r = infect2(matrix, i+1, j)
    d = infect2(matrix, i, j+1)
    u = infect2(matrix, i, j-1)
    return 1 + l + r + d + u

def count_island(matrix):
    if len(matrix) == 0 or len(matrix[0]) == 0:
        return 0
    res = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1:
                res += 1
                island_num = infect2(matrix, i, j)
                print("island_num:", island_num)
    return res
    

"""  
扩展:
    如果矩阵是一个巨大的数组，有多个cpu，如何分配任务和合并结果。
    合并的时候如何操作，使用并查集
        假如分为两个矩阵，遍历到每一个岛的时候，将每个岛的第一元素设为该岛的头
        对于每一个子矩阵，返回矩阵内岛的数量和边界节点的头信息。
        依次对比两个矩阵的边界，如果两个节点都是1，且头不同，合并，岛数量减1，头相同跳过
        分为多个矩阵，就保存四个边界。
"""


if __name__ == "__main__":
    matrix = [[0 for i in range(3)] for i in range(4)]
    matrix = [[0,0,1],[0,1,0],[1,1,1]]
    print(count_island(matrix))

