# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        result = self.helper(1, n)
        return result 

    def helper(self, low, high):
        mid = (low + high) // 2
        result = guess(mid)
        if result == 0:
            return mid
        # 1 is lower
        elif result == -1:
            return self.helper(low, mid -1)
        # -1 is higher
        elif result == 1:
            return self.helper(mid+1, high)


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna