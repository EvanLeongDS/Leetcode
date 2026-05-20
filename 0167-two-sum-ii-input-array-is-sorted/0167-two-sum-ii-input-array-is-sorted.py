class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # establish the two pointers
        n = len(numbers)
        l = 0 
        r = n - 1

        while l < r:
            # if our current sum is too big move the right index down a bit 
            if numbers[l] + numbers[r] > target:
                r -= 1
            # if our current sum is too small move the left index up a bit
            elif numbers[l] + numbers[r] < target:
                l += 1  
            # get the 1 index from our two sum 
            else:
                return [l + 1, r + 1]


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna