class Solution:
    def numDecodings(self, s: str) -> int:
        # create a 1d table the length of the string
        n = len(s) + 1

        dp = [0] * n
        dp[0] = 1
        
        # build the table
        for i in range(1, n):
             # Rule 1: single digit s[i-1] is valid if it's not '0'
            if s[i-1] != "0":
                dp[i] += dp[i-1]

            # Rule 2: pair s[i-2:i] is valid if i >= 2 and it's between 10-26
            if i >= 2 and 10 <= int(s[i-2:i]) <= 26:
                dp[i] += dp[i - 2]
            
        return dp[n - 1]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna