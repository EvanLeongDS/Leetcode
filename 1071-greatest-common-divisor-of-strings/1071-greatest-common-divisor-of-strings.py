class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # find prefix 
        prefix_str = ""
        min_len = min(len(str1), len(str2))
        for i in range(min_len):
            if str1[i] == str2[i]:
                prefix_str += str1[i]
            else:
                break

        # slice the prefix down until it evenly divides both strings
        while len(prefix_str) > 0:
            plen = len(prefix_str)
            if len(str1) % plen == 0 and len(str2) % plen == 0:
                if prefix_str * (len(str1)//plen) == str1 and prefix_str * (len(str2)//plen) == str2:
                    return prefix_str
            prefix_str = prefix_str[:-1]

        return ""

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna