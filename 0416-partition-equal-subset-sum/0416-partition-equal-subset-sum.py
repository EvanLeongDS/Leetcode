class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # establish empty table and the target subset
        n = len(nums) + 1
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = sum(nums) // 2

        dp = [False] * (target + 1)


        # base case
        dp[0] = True # vacuously true 
        
        # build table over every number until we get to the target 
        for num in nums:
            for t in range(target, num - 1, -1):   # inner: each sum
                dp[t] = dp[t] or dp[t - num]
        return dp[target]
        
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna