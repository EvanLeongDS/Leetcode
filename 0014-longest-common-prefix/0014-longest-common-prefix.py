class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Find the longest common prefix string amonst an array of strings 

        prefix = ""
        # iterate over the first string 
        for i in range(len(strs[0])):
            # iterate over all other strings 
            for j in range(1, len(strs)):
                # make sure the string goes that far before it goes out of bounds
                if i >= len(strs[j]):
                    return prefix
                # compare whether strs[0][i] is equivalent to strs[j][i]
                if strs[0][i] != strs[j][i]:
                    return prefix
            prefix += strs[0][i]
        return prefix

            



        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna