class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        def backtrack(index, current):
            if index == len(s):
                result.append(current[:])
                return
            for i in range(index, len(s)):
                if s[index:i+1] == s[index:i+1][::-1]:
                    current.append(s[index:i+1])
                    backtrack(i + 1 , current)
                    current.pop()
        backtrack(0, [])
        return result 

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna