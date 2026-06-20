class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        def backtrack(current, seen):
            if len(current) == len(nums):
                result.append(current[:])
                return 

            # loop through all nums until we complete the permutation
            for i in range(len(nums)):
                if nums[i] not in seen:
                    # recurse down 
                    seen.add(nums[i])
                    current.append(nums[i])
                    backtrack(current, seen)
                    current.pop()
                    seen.remove(nums[i])

        backtrack([], set())
        return result

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna