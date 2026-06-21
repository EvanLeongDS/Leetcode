class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # map digits to letters using a dictionary
        phone = {
                "2": "abc", "3": "def", "4": "ghi",
                "5": "jkl", "6": "mno", "7": "pqrs",
                "8": "tuv", "9": "wxyz"
            }
        result = []
        def backtrack(index, current):
            if index == len(digits):
                result.append(current[:])
                return
            
            # loop through all digits and get the values 
            digit = digits[index]
            letters = phone[digit]
            for letter in letters:
                backtrack(index + 1, current + letter)

        backtrack(0, "")
        return result

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna