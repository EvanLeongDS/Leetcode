class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        output = [] # will return length of interval 
        letter_dict = {}
        for index, letter in enumerate(s):
            if letter not in letter_dict:
                letter_dict[letter] = index
            elif letter in letter_dict and index > letter_dict[letter]:
                letter_dict[letter] = index

        # second pass for output 
        start = 0
        end = 0 # find the end of the window
        for i in range(len(s)):
            end = max(end, letter_dict[s[i]])
            if i == end:
                output.append(end - start + 1)
                start = i + 1
        return output

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna