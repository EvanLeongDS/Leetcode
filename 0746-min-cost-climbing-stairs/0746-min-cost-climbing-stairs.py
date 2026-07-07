class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # take one step or two steps depending on what has a lower cost 
        dp = [0] * (len(cost) + 1)
        # base case 1 step just take that 2 just take the lower
        dp[0] = 0
        dp[1] = 0
        for i in range(2, (len(cost) + 1)):
            dp[i] = min(dp[i - 2] + cost[i - 2], dp[i - 1] + cost[i - 1])
        return dp[len(cost)]


        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna