class Solution:
    def longestPalindrome(self, s: str) -> str:
        # base case: if you have 1 character in the string just return the string 
        if len(s) <= 1:
            return s
        if len(s) == 2 and s[0] == s[-1]:
            return s 
        max_len = 1
        max_str = s[0]

        # establish empty dp list of false booleans change them to true later
        dp = [[False for _ in range(len(s))] for _ in range(len(s))]

        # build a 2d table 
        for i in range(len(s)):
            dp[i][i] = True
            for j in range(i):
                if s[j] == s[i] and (i - j < 2 or dp[j+1][i-1] is True):
                    dp[j][i] = True
                    if len(s[j:i+1]) > max_len:
                        max_len = len(s[j:i+ 1])
                        max_str = s[j:i+1]
        return max_str

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna