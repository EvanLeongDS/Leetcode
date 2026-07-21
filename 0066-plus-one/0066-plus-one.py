class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits) - 1 
        my_sum = 0 
        result = []
        for digit in digits:
            my_sum += digit * (10 ** n)
            n = n - 1
        
        # add one more for that plus one
        my_sum += 1
        while my_sum > 0:
            result.append(my_sum % 10)
            my_sum =  my_sum // 10
        result.reverse()
        return result
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna