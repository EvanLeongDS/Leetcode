class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        my_set = set()
        for num in nums: 
            if num not in my_set:
                my_set.add(num)
            else:
                my_set.remove(num)
        return next(iter(my_set))
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna