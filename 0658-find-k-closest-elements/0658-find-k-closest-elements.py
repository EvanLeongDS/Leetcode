class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # the array is sorted and we compare them if they are sorted or not 
        left = 0
        right = len(arr) - 1
        n = len(arr)
        # delete elements until we have a fully refined list 
        while n > k:
            if abs(arr[left] - x) < abs(arr[right] - x): 
                right -= 1
                n -= 1
            elif abs(arr[left] - x) == abs(arr[right] - x) and arr[left] < arr[right]:
                right -= 1
                n -= 1
            else:
                left += 1
                n -= 1
        return arr[left:right + 1] 

            
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna