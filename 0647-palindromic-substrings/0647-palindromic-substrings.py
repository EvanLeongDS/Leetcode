class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0 # will return in the end 
        if len(s) == 1:
            return 1
        if len(s) == 2 and s[0] == s[-1]:
            return 3
        dp = [[False for _ in range(len(s))] for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = True # single characters are always palindromes, therefore increase the count 
            count += 1
            for j in range(i):
                # evaluate if something is a palindrome and build from there
                if s[j] == s[i] and (i - j < 2 or dp[j+1][i-1] is True):
                    # if you reach the base case of there being 2 or less characters or the next characteres up are equal you can also increase the count 
                    dp[j][i] = True
                    count += 1
        return count
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna