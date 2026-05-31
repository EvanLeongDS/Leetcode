class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0 
        high = len(nums) - 1 

        while low <= high: 
            mid = (low + high) // 2 
            print(mid)
            if nums[mid] == target:
                return mid 
            elif nums[low] <= target < nums[mid]:
                #  1 2 3 4 5 target is 2 we know left side is sorted search there
                high = mid - 1 
            elif nums[mid] < target <= nums[high]:
                # right side is sorted we can search there
                low = mid + 1 
            elif nums[low] <= nums[mid]:
                # we know the left side is sorted and we know target is not in there so search right side 
                low = mid + 1 
            else:
                # we know the right side is sorted and target is not in there so search left side
                high = mid - 1 
        return -1

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna