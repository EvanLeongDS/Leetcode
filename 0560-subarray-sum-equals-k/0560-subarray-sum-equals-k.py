class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        prefix_sum = {0: 1}
        total = 0 
        for i, num in enumerate(nums):
            total += num
            if total - k in prefix_sum:
                count += prefix_sum[total - k]
            if total in prefix_sum:
                prefix_sum[total] += 1
            else:
                prefix_sum[total] = 1
        return count