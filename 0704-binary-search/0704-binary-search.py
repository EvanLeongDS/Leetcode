import math
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo = 0
        hi = len(nums) - 1
        mid = math.floor((lo + hi)/2)
        while lo <= hi:
            mid = math.floor((lo + hi)/2)
            if target == nums[mid]:
                return mid
            elif target > nums[mid]: # search right side 
                lo = mid + 1
            else:
                hi = mid - 1
        return -1
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna