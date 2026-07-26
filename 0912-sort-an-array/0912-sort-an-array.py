class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # do divide and conquer, do a merge sort 

        # base case 
        if len(nums) <= 1:
            return nums
        # split in half and recursively divide 
        mid = len(nums) // 2
        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])
        
        # combine together
        return self.merge(left, right)
    def merge(self, left, right):
        # take the left side and right side and put it back together
        result = []
        while left and right:
            if left[0] < right[0]:
                result.append(left[0])
                left.pop(0)
            else:
                result.append(right[0])
                right.pop(0)
        # add remaining items
        result += left
        result += right
        return result

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna