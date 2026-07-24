class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0 
        for _ in range(32):
            bit = n & 1
            result = (result << 1) | bit 
            n = n >> 1
        return result

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna