class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        def backtrack(index, current):
            if index == len(nums):
                result.append(current[:])
                return
        
            # take index
            current.append(nums[index])
            backtrack(index + 1, current)  
            current.pop()

            # leave index
            backtrack(index + 1, current) 
        backtrack(0, [])
        return result

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna