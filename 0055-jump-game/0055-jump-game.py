class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # greedily take the steps in front of you 
        farthest = 0
        for i in range(len(nums)):
            if i > farthest:
                return False
            if farthest >= len(nums) - 1:
                return True
            farthest = max(farthest, i + nums[i])
        return False
        