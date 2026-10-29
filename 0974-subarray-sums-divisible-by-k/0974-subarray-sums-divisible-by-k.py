class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        seen = {0:1}
        prefix = 0 
        count = 0 # number of subarrays that have a sum divisible by k 

        for num in nums:
            prefix += num
            count += seen.get(prefix % k, 0)

            if prefix % k not in seen:
                seen[prefix % k] = 1
            else:
                seen[prefix % k] += 1
        return count 