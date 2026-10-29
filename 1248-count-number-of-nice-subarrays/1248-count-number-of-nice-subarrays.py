class Solution:
    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
        prefix = 0
        count = 0
        seen = {0:1}

        for num in nums:
            # add an odd number to the prefix sum
            if num % 2 != 0:
                prefix += 1
            count += seen.get(prefix - k, 0)

            if prefix not in seen:
                seen[prefix] = 1
            else:
                seen[prefix] += 1
        return count
        