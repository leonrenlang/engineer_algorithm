# 问题： 9*9的矩阵，每个格子里可以放1-9,要求行列无重复元素
# 并且将矩阵划分成3*3个3*3的小矩阵，小矩阵内也无重复元素


# 思想：
# - https://labuladong.gitbook.io/algo/suan-fa-si-wei-xi-lie/sudoku
# - 回溯法
# - 选择列表：对于每个格子，其选择列表就是1-9，需要考虑其所在行，列，3*3方格是否又重复元素
# 子问题的选择列表与父问题同
# - 路径：采用一个9*9的矩阵保存已经做出的选择
# - 终止条件，得到一个满足条件的解


def backtrack(board, i, j):
    m, n = 9, 9
    if j == n:
        return backtrack(board, i + 1, 0)
    if i == m:  # 找到一个可行解，触发base case
        return True
    if board[i][j] != '.':
        return backtrack(board, i, j + 1)
    for ch in range(1, 10):
        if not is_valid(board, i, j, ch):
            continue
        board[i][j] = ch
        if backtrack(board, i, j + 1):
            return True
        board[i][j] = '.'

    return False


def is_valid(board, r, c, ch):
    for i in range(9):
        if board[r][i] == ch: return False
        if board[i][c] == ch: return False
        # 太巧妙了！！！判断该元素所属的3*3小方格无重复元素
        if board[(r / 3) * 3 + i / 3][(c / 3) * 3 + i % 3] == ch:
            return False
    return True
