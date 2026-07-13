class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # establish empty dp table
        m = len(s)
        n = len(t)

        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        # build base cases
        for i in range(m + 1):
            dp[i][0] = 1 # its 1 since there is 1 way to delete shi until you have nothing left
        for j in range(1, n + 1):
            dp[0][j] = 0 # you cant delete anything if there is nothing there
       
        # build table 
        for i in range(1, m + 1): # for the s string
            for j in range(1, n + 1): # for the t string 
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j] 
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[m][n]  # for indexing      

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna