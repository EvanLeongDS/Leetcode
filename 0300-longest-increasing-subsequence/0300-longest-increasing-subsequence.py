class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # establish table 
        n = len(nums)
        dp = [1] * n 

        #  establish table 
        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i]= max(dp[i], dp[j] + 1)
        return max(dp) # the maximum value could be in the middle not necessarily the end

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna