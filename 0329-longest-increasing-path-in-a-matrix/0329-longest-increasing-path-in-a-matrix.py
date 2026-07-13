class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # establish empty dp table 
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        longest_path = 0 # return variable

        # do the base case where its just 1
        for i in range(m):
            for j in range(n):
                path = self.dfs(dp, i, j, matrix, m, n) 
                if path > longest_path:
                    longest_path = path
        return longest_path

    def dfs(self, dp, i, j, matrix, m, n):   
        if dp[i][j] != 0:
            return dp[i][j]

        best = 1
        for direction in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                    new_row = i + direction[0]
                    new_col = j + direction[1]
                    if 0 <= new_row < m and 0 <= new_col < n:
                        if matrix[new_row][new_col] > matrix[i][j]:
                            neighbor_path = self.dfs(dp, new_row, new_col, matrix, m, n)
                            best = max(best, 1 + neighbor_path)
        dp[i][j] = best
        return dp[i][j]


        
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna