class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1) + 1
        n = len(text2) + 1
        dp = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(1, m):
            for j in range(1, n):
                if text1[i-1] == text2[j-1]:
                    # we can examine the i-1 and j-1 letters
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    # drop one character and use the best one from the previous subsequences
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[m-1][n-1]
        

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna