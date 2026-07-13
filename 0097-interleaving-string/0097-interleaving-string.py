class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # establish empty dp table 
        m = len(s1)
        n = len(s2)
        dp = [[False for _ in range(n + 1)] for _ in range(m+1)]

        # base check
        if (m + n) < len(s3) or (m+n) > len(s3):
            return False
        # base case 
        dp[0][0] = True # vacuously true
        for i in range(1, m+1): # first row
            if s1[0:i] == s3[0:i]:
                dp[i][0] = True
        for j in range(1, n+1):
            if s2[0:j] == s3[0:j]:
                dp[0][j] = True
        
        # build dp table 
        for i in range(1, m+1):
            for j in range(1, n+1):
                # evaluate smaller cases using interleaving 
                if (s1[i-1] == s3[i + j -1] and dp[i-1][j] is True) or (s2[j-1] == s3[i + j - 1] and dp[i][j-1] is True):
                    dp[i][j] = True
        return dp[m][n]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna