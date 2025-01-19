class Solution:
    def exist(self, board, word: str) -> bool:
        # 使用深度优先搜索
        if not board:  # 边界条件
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, i, j, word):
                    return True
        return False

    def exist(self, board, word):
        if not board: return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, i, j, word):
                    return True
        return False

    def dfs(self, board, i, j, word):
        if len(word) == 0:  # 如果单词已经检查完毕
            return True
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or word[0] != board[i][
            j]:  # 如果路径出界或者矩阵中的值不是word的首字母，返回False
            return False
        tmp = board[i][j]  # 如果找到了第一个字母，检查剩余的部分
        board[i][j] = '0'
        res = self.dfs(board, i + 1, j, word[1:]) or self.dfs(board, i - 1, j, word[1:]) or self.dfs(board, i, j + 1,
                                                                                                     word[
                                                                                                     1:]) or self.dfs(
            board, i, j - 1, word[1:])  # 上下左右四个方向搜索

        board[i][j] = tmp
        return res

    def dfs(self, board, i, j, word):
        if len(word) == 0:
            return True
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            pass



def main():
    pass
