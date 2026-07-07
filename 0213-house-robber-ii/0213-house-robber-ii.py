class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        first_slice = nums[1:]
        last_slice = nums[:-1]
        first_count = self.rob_choice(first_slice)
        last_count = self.rob_choice(last_slice)
        return max(first_count, last_count)

        
            
    def rob_choice(self, nums):
        # establish empty 1d table 
        n = len(nums) + 1
        dp = [0] * n

        # base cases
        dp[0] = 0
        dp[1] = nums[0]
        for i in range(2, n):
            # set recurrence with the idea that you cannot have the first and last haouse together 
            dp[i] = max(nums[i-1] + dp[i-2], dp[i-1])
        return dp[n - 1]


            

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna