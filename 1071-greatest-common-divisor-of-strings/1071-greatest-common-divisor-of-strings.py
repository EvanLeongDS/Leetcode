class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def gcd(a, b):
            if b == 0:
                return a
            return gcd(b, a % b)

        g = gcd(len(str1), len(str2))
        prefix_str = str1[:g]

        if len(prefix_str) > 0 and prefix_str * (len(str1) // len(prefix_str)) != str1:
            prefix_str = ""
        if len(prefix_str) > 0 and prefix_str * (len(str2) // len(prefix_str)) != str2:
            prefix_str = ""
        return prefix_str

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna