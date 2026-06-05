class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res= ""
        for i in range(len(strs[0])):
            matching_char = strs[0][i]
            print(matching_char)
            for string in strs:
                if i == len(string) or string[i] != matching_char:
                    return res
            res += matching_char
        return res

            



        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna