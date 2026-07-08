import math
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # establish some basic if statements
        if amount == 0:
            return 0 
        # establish empty dp table in accordance to the amount 
        n = amount + 1
        dp = [math.inf] * n 
        # base case
        dp[0] = 0 

        # recurrence is take it or dont take it 
        for i in range(1, n):
            for coin in coins:
                if coin <= i:
                    dp[i] = min(1 + dp[i - coin], dp[i])

        if dp[n - 1] == math.inf:
            return -1
        return dp[amount]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna