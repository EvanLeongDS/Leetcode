import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1 # can't eat 0 bananas
        high = max(piles) # max of whatever the pile is 
        
        while low <= high:
            mid = (low + high) // 2

            # find piles / speed to find the hours per pile 
            total_hours = 0
            for pile in piles:
                hours = math.ceil(pile / mid)
                total_hours += hours

            if total_hours > h:
                # we are eating too slow gotta speed it up
                low = mid + 1
            else:
                # we are eating too fast we can scale high down
                high = mid - 1
        return low 


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna