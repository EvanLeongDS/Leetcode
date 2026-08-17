class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combo_list = []

        def backtrack(start, path):
            if len(path) == k:
                combo_list.append(path[:])
                return

            for i in range(start, n + 1):
                path.append(i)
                backtrack(i+1, path)
                path.pop()

        backtrack(1, [])
        return combo_list

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna