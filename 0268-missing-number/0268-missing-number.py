class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        num_set = set()
        for i in range(n + 1):
            num_set.add(i)
        for num in nums:
            if num in num_set:
                num_set.remove(num)
        return num_set.pop()
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna