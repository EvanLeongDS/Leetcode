class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0 
        high = len(nums) - 1 

        # check if target is outside the scope of nums
        if target < nums[0]:
            return 0 
        if target > nums[-1]:
            return len(nums)
        
        # conduct binary search algorithm
        while low <= high:
            mid = (low + high) // 2
            # Check if the midpoint is indeed equal to the target
            if nums[mid] == target:
                return mid 
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        print(low, high, mid, target)
        return low


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna