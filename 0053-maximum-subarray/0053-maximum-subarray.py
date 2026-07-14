class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = nums[0]
        max_so_far = nums[0]
        # go through the loop and if a new number is greater than the current sum we reset the window
        for i in range(2, (len(nums) + 1)):
            if nums[i-1] > current_sum + nums[i-1]: # make sure it extends
                current_sum = nums[i-1]
            else:
                current_sum += nums[i-1]
            if current_sum > max_so_far:
                max_so_far = current_sum 

        return max_so_far
        