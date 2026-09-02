class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low = max(weights)
        high = sum(weights)
        
        mid = (low + high) // 2
        best = high
        while low <= high:
            mid = (low + high) // 2
            temp = mid
            temp_days = 0
            for i in range(len(weights)):
                temp -= weights[i]
                if temp < 0:
                    temp_days += 1
                    temp = mid - weights[i]
            temp_days += 1
            if temp_days <= days:
                best = mid
                high = mid - 1
            else:
                low = mid + 1 
        return best


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna