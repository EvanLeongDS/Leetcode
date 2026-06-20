class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def backtrack(current, left_count, right_count):
            if len(current) == 2 * n:
                result.append(current)
                return
            
            # add some parenthesis 
            if left_count < n:
                backtrack(current + "(", left_count + 1, right_count)
            if right_count < left_count:
                backtrack(current + ")", left_count, right_count + 1)
        backtrack("", 0, 0)
        return result
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna