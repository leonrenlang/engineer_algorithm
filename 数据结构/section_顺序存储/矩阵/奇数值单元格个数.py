# 给你一个 n 行 m 列的矩阵，最开始的时候，每个单元格中的值都是 0。
# 另有一个索引数组 indices，indices[i] = [ri, ci] 中的 ri 和 ci 分别表示指定的行和列（从 0 开始编号）。
# 你需要将每对 [ri, ci] 指定的行和列上的所有单元格的值加 1。
# 请你在执行完所有 indices 指定的增量操作后，返回矩阵中 「奇数值单元格」 的数目。
# 示例 1：
# 输入：n = 2, m = 3, indices = [[0,1],[1,1]]
# 输出：6
# 解释：最开始的矩阵是 [[0,0,0],[0,0,0]]。
# 第一次增量操作后得到 [[1,2,1],[0,1,0]]。
# 最后的矩阵是 [[1,3,1],[1,3,1]]，里面有 6 个奇数。

def process(n, m, indices):
    dic_row = {}
    dic_col = {}
    res = 0
    for i in range(n):
        dic_row[i] = 0
    for j in range(m):
        dic_col[j] = 0
    for indice in indices:
        dic_row[indice[0]] += 1
        dic_col[indice[1]] += 1
    for i in range(n):
        for j in range(m):
            if (dic_row[i] + dic_col[j]) % 2 == 1:
                res += 1
    return res


if __name__ == '__main__':
    n = 2
    m = 3
    indices = [[0, 1], [1, 1]]
    print(process(n, m, indices))
