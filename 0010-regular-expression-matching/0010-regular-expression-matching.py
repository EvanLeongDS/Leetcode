class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # build dp table 
        m = len(s)
        n = len(p)
        dp = [[False for _ in range(n+1)] for _ in range(m+1)]
        
        # base case 
        dp[0][0] = True # vacuously true

        # check empty s where there can be a star
        for j in range(1, n+1):
            if p[j-1] == '*':
                dp[0][j] = dp[0][j-2]

        # build table
        for i in range(1, m+1):
            for j in range(1, n+1):
                if p[j-1] == '*':
                    dp[i][j] = dp[i][j-2] or ((s[i-1] == p[j-2] or p[j-2] == '.') and dp[i-1][j])
                elif s[i-1] == p[j-1] or p[j-1] == '.':
                    dp[i][j] = dp[i-1][j-1] # match so we can disregard those characters
                else:
                    dp[i][j] = False
        return dp[m][n]