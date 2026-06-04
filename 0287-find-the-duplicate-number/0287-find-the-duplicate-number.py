class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]       
        fast = nums[nums[0]]
        
        # keep jumping around until slow and fast reach an agreement
        while slow != fast:
            slow = nums[slow]
            fast= nums[nums[fast]]
        
        # do another loop and wait until they meet once slow is rest
        slow = 0 
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna