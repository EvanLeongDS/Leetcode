class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        my_dict = {}
        for num in nums:
            if num not in my_dict:
                my_dict[num] = 1 
            else:
                my_dict[num] += 1
        max_key = 0
        max_value = 0 
        for key, value in my_dict.items():
            if value > max_value:
                max_value = value
                max_key = key
        return max_key

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna