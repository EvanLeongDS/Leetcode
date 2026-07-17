class Solution:
    def checkValidString(self, s: str) -> bool:
        low = 0
        high = 0
        for char in s:
            if high < 0:
                return False
            elif char == "(":
                low += 1
                high += 1
            elif char == "*":
                low = max(0, low - 1)
                high += 1
            elif char == ")":
                low = max(0, low - 1)
                high -= 1
            if high < 0:
                return False
        if low == 0:
            return True
        else:
            return False

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna