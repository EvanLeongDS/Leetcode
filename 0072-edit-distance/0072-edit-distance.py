class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # establish empty dp table 
        m = len(word1)
        n = len(word2)

        dp = [[0 for _ in range(n + 1)] for _ in range(m+1)]

        # base cases
        # empty word 2 
        for i in range(m + 1):
            dp[i][0] = i # i letters to delete to get to nothing 
        # empty word 1
        for j in range(1, n+1):
            dp[0][j] = j # j inserts to get to j 

        # build table 
        for i in range(1, m+1):
            for j in range(1, n+1):
                # recurrence 
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1] # no need to do anything move down
                else: # leave it 
                    # three options are insert, delete, replace
                    dp[i][j] = 1 + min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])
        return dp[m][n]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna