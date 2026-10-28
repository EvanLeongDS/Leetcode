class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        left_prefix = [] # sum the numbers up from left to right in a prefix array
        right_prefix = [] # sum the numbers up from right to left in a prefix array
        n = len(nums)

        left_sum = 0 
        right_sum = 0
        for i in range(n):
            left_sum += nums[i]
            right_sum += nums[n-1-i]

            left_prefix.append(left_sum)
            right_prefix.append(right_sum)
        print(left_prefix, right_prefix)

        for i in range(n):
            if left_prefix[i] == right_prefix[n-1-i]:
                return i
        return -1
