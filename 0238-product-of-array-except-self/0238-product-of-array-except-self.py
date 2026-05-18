import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # split into two lists
        n = len(nums)
        left_list = [1] * n
        right_list = [1] * n
        
        # [1, 1, 2, 6]
        # [24, 12, 4, 1]
        for i in range(1, n):
            left_list[i] = left_list[i-1] * nums[i-1]
        for i in range(n - 2, -1, -1):
            right_list[i] = right_list[i+1] * nums[i+1]

        print(left_list)
        print(right_list)

        output = []
        for i in range(n):
            # multiply everything
            product = left_list[i] * right_list[i]
            output.append(product)
        return output 



# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna