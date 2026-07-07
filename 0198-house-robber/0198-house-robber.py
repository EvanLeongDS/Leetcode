class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0] * (len(nums) + 1)
        # base cases
        dp[0] = 0
        dp[1] = nums[0]
        
        # iterate to build table 
        for i in range(2, len(nums) + 1):
            # maximize robbings by either looting the house or skipping 
            dp[i] = max(nums[i - 1] + dp[i-2], dp[i-1])
        return dp[len(nums)]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna