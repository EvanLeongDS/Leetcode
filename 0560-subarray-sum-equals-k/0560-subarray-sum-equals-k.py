class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = 0  # prefix sum
        seen = {0: 1}
        count = 0 # number of times subarray sum equals k 

        for num in nums:
            prefix += num
            count += seen.get(prefix - k, 0)

            if prefix not in seen:
                seen[prefix] = 1
            else:
                seen[prefix] += 1

        return count