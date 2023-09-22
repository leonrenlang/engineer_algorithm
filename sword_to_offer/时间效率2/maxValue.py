

# 礼物的最大价值
'''
在一个 m*n 的棋盘的每一格都放有一个礼物，每个礼物都有一定的价值（价值大于 0）。
你可以从棋盘的左上角开始拿格子里的礼物，并每次向右或者向下移动一格、直到到达棋盘的右下角。
给定一个棋盘及其上面的礼物的价值，请计算你最多能拿到多少价值的礼物？
'''
# 思路：f(i, j) = max(f(i - 1, j), f(i, j-1)) + gift[i, j])


class Solution:
    def maxValue(self, grid):
        '''
        :type grid: List[List[int]]
        :rtype: int
        '''
        if grid==[] or grid==[[]]:  return 0
        m = len(grid)
        n = len(grid[0])
        for i in range(1,n):                    # 先更新第一行和第一列的值
            grid[0][i] += grid[0][i-1]
        for j in range(1, m):
            grid[j][0] += grid[j-1][0]

        for i in range(1,m):                # 更新其他行列的值
            for j in range(1,n):
               grid[i][j] = max(grid[i-1][j]+grid[i][j],grid[i][j-1]+grid[i][j]) 
        return grid[m-1][n-1]
