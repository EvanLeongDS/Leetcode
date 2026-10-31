import math 
class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        if m == 1 and n == 1:
            return grid[0][0]

        # build dp table 
        dp = [[math.inf for _ in range(n)] for _ in range(m)]

        # base case 
        dp[0][0] = grid[0][0]

        # build the edges 
        row_sum = grid[0][0]
        for i in range(1, m):
            row_sum += grid[i][0]
            dp[i][0] = row_sum
        
        col_sum = grid[0][0]
        for j in range(1, n):
            col_sum += grid[0][j]
            dp[0][j] = col_sum
        
        # the choice might be to choose the minimum between the left and the top 
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(grid[i][j] + dp[i-1][j], grid[i][j] + dp[i][j-1])
        
        print(dp)
        return dp[m-1][n-1]