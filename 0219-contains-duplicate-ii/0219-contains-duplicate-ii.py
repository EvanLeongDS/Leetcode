from typing import List
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window_set = set()
        for i in range(len(nums)):
            # remove things out of window
            if i > k:
                window_set.remove(nums[i - k - 1])
            # check if a new element is in the set 
            if nums[i] in window_set:
                return True
            window_set.add(nums[i])
        return False

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna