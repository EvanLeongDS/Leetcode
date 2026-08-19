class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        my_string = ""
        while columnNumber > 0:
            remainder = (columnNumber - 1) % 26
            letter = chr(65 + remainder)
            my_string = letter + my_string 
            columnNumber = (columnNumber - 1) // 26
            print(columnNumber)
        return my_string

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna