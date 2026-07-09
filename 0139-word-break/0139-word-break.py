class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s) + 1
        # establish empty array and base case
        dp = [False] * n
        dp[0] = True # vacuously true
        words = set(wordDict) # make it a set so O(1) lookup and 
        # build table 
        for i in range (1, n):
            for j in range(i):
                if dp[j] and s[j:i] in words:
                    dp[i] = True
        print(dp)
        return dp[len(s)]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna