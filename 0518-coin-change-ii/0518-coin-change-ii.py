class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        m = len(coins)
        n = amount
        # establish empty dp table 
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        # base case
        dp[0][0] = 1 # when we hit this base case return 1 therefore done

        # build table
        # recurrence is to take a coin or to not take it 
        for i in range(1, m + 1):
            for j in range(n + 1):
                dp[i][j] = dp[i-1][j] # factor in alternative coins
                if coins[i-1] <= j:
                    dp[i][j] += dp[i][j - coins[i-1]]
        return dp[m][n]


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna