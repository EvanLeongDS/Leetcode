class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0 # pointer to move numbers around 
        for i in range(len(nums)):
            if nums[i] == val:
                pass
            else:
                nums[k] = nums[i]
                k += 1
        print(nums)
        return k 
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna