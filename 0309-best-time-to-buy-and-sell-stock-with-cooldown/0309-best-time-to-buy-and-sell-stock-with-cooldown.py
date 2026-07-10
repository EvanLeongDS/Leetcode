import math

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        # dp[i] = [hold, sold, rest] for day i
        # Extra row at index 0 = base case "before any day"
        dp = [[0, 0, 0] for _ in range(n + 1)]

        dp[0][0] = -math.inf   # hold: can't own a stock yet
        dp[0][1] = 0           # sold: $0
        dp[0][2] = 0           # rest: $0

        # loop goes here
        for i in range(1, n + 1):
            price = prices[i-1]
            dp[i][0] = max(dp[i-1][0], dp[i-1][2] - price) # hold
            dp[i][1] = dp[i-1][0] + price #sold
            dp[i][2] = max(dp[i-1][1], dp[i-1][2]) # rest
        return max(dp[n][0], dp[n][1], dp[n][2])

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna