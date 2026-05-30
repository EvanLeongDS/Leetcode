import math
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0]) if m > 0 else 0
        low = 0
        high = (m * n) - 1

        # conduct binary search
        while low <= high:
            mid = math.floor((low + high) / 2)
            row = math.floor(mid / n)
            col = mid % n
            
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                # we need to think smaller
                # move lo upward and examine right side 
                high = mid - 1
            else:
                # we need to think bigger
                # move high downward and examine left side
                low = mid + 1

        # binary search found nothing, therefore return false       
        return False
        
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna