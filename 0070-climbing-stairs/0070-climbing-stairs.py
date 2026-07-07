class Solution:
    def climbStairs(self, n: int) -> int:
        # case 1 you take 1 step case 2 you take two steps
        dp = [0] * (n + 1)

        if n <= 2:
            return n
        # handle base cases
        dp[0] = 0
        dp[1] = 1
        dp[2] = 2

        # build table using a for loop 
        for i in range(3, n+1):
            # use recurrence
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna