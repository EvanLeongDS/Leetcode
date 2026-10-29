class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        # if the length is at least two and the sum is a multiple of k 
        prefix = 0 
        seen = {0:-1}

        for i in range(len(nums)):
            prefix += nums[i]
            
            if (prefix % k) in seen:
                length = i - seen[prefix % k]
                if length >= 2:
                    
                    return True

            if prefix % k not in seen:
                seen[prefix % k] = i

        return False