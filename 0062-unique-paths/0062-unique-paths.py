class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # build empty table 
        dp = [[1 for _ in range(n)] for _ in range(m)]

        # no need for base cases since we already established them while creating dp 

        # To reach any cell, you add together the number of ways to reach the cell directly above it and the cell directly to its left, because those are the only two cells a robot could have stepped from.
        for i in range(1, m): # m rows
            for j in range (1, n): # n columns
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m - 1][n - 1]



        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna