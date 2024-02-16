# 问题79：给定一个二维网格和一个单词，找出该单词是否存在于网格中。
# 单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。
# 同一个单元格内的字母不允许被重复使用。

# 思想： 遍历矩阵中的每个元素，暴力回溯，判断结果
class Solution:
    def exist(self, board, word: str) -> bool:
        row = len(board)
        col = len(board[0])

        def helper(i, j, k, visited):
            if k == len(word):
                return True
            for x, y in [(-1, 0), (1, 0), (0, 1), (0, -1)]:  # 遍历一个元素相邻的元素
                tmp_i = x + i
                tmp_j = y + j
                if 0 <= tmp_i < row and 0 <= tmp_j < col and (tmp_i, tmp_j) not in visited \
                        and board[tmp_i][tmp_j] == word[k]:
                    visited.add((tmp_i, tmp_j))
                    if helper(tmp_i, tmp_j, k + 1, visited):
                        return True
                    visited.remove((tmp_i, tmp_j))
            return False

        for i in range(row):
            for j in range(col):
                if board[i][j] == word[0] and helper(i, j, 1, {(i, j)}):  # 用于装已经用过元素是一个集合
                    return True
        return False


board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word = "ABCB"
print(Solution().exist(board, word))
