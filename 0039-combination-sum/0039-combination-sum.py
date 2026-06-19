class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        def backtrack(index, current, target):
            if target == 0:
                result.append(current[:])
                return
            if target < 0:
                return 
            if index == len(candidates):
                return

            # pick a candidate
            current.append(candidates[index])
            backtrack(index, current, target - candidates[index])  
            current.pop()
            # skip a candidate
            backtrack(index + 1, current, target) 


        backtrack(0, [], target)
        return result

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna