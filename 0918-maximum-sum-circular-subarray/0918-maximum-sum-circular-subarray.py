import math
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # establish fundamental variables
        max_sum = -math.inf
        min_sum = math.inf
        curr_sum = 0 
        curr_sum2 = 0 
        n = len(nums)
        total = sum(nums)
        
        # iterate to find subarrays
        for i in range(n):
            curr_sum += nums[i]
            curr_sum2 += nums[i]
            max_sum = max(curr_sum, max_sum)
            min_sum = min(min_sum, curr_sum2)

            if curr_sum < 0:
                curr_sum = 0 
            if curr_sum2 > 0:
                curr_sum2 = 0 
            
        # handle wrap_sum 
        wrap_sum = total - min_sum
        if max_sum > 0:
            max_sum = max(max_sum, wrap_sum)
        else:
            return max_sum
        return max_sum

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna