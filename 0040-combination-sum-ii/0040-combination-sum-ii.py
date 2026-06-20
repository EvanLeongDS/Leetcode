class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()
        def backtrack(index, current, target):
            # base cases
            if target == 0:
                result.append(current[:])
            if target < 0:
                return
            if index == len(candidates):
                return
            
            # if duplicate number kill the branch 
            seen = set()
            for i in range(index, len(candidates)):
                if candidates[i] in seen:
                    continue
                seen.add(candidates[i])
                current.append(candidates[i])
                backtrack(i + 1, current, target - candidates[i])
                current.pop()
            
           

        backtrack(0, [], target)
        return result
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna