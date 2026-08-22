class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        def backtrack(index, current):
            if len(current) == k:
                result.append(current[:])
                return
            for j in range(index, n + 1):
                current.append(j)
                backtrack(j + 1, current)
                current.pop()
        backtrack(1, [])
        return result

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna