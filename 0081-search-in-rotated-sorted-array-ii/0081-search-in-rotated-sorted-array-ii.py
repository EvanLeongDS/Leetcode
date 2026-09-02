class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        low = 0
        high = len(nums) - 1
        mid = (low + high) // 2

        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return True 
            elif nums[low] == nums[mid] == nums[high]:
                low += 1 
                high -= 1
            elif nums[low] <= nums[mid]:
                # the left half is sorted
                if nums[low] <= target <= nums[mid]:
                    # we know target is in the left side 
                    high = mid - 1
                else:
                    low = mid + 1 
            elif nums[low] > nums[mid]:
                # the right half is sorted 
                if nums[mid] <= target <= nums[high]:
                    # # we know the target is in the right side 
                    low = mid + 1 
                else:
                    high = mid - 1
        return False

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna