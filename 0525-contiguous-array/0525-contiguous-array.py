class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        seen = {0: -1}
        prefix = 0 
        best = 0

        for index, num in enumerate(nums):
            if num == 0:
                prefix -= 1
            elif num == 1:
                prefix += 1
            
            if prefix in seen:
                length = index - seen[prefix]
                best = max(best, length)
            else:
                seen[prefix] = index

        return best
