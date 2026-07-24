class Solution:
    def reverse(self, x: int) -> int:
        negative = False
        if x < 0 :
            negative = True 
        result = 0 
        x = abs(x)
        while x != 0:
            digit = x % 10
            result = result * 10 + digit
            x = x // 10 
        
        # double check for original negative
        if result > 2**31 - 1:
            return 0
        if negative:
            return -result 
        else:
            return result 
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna