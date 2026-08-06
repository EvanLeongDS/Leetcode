class Solution:
    def mySqrt(self, x: int) -> int:
        # base case
        if x ==0:
            return 0 
        if x == 1:
            return 1 
        low = 1
        high = x
        while low <= high:
            mid = (low + high) // 2
            if mid * mid == x:
                return mid 
            elif mid * mid < x and (mid+1) * (mid+1) > x:
                return mid
            elif mid * mid < x:
                # too small, therefore we want to search the upper half 
                low = mid + 1
            else:
                # too big. therefore search the lower half 
                high = mid - 1


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna