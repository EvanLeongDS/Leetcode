class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0 
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == nums[high]:
                return nums[mid]
            elif nums[mid] < nums[high]:
                # search the left side
                high = mid
            else:
                low = mid + 1 

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna