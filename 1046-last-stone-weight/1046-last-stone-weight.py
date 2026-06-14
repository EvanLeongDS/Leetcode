import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 0:
            return 0 
        heapq.heapify_max(stones)
        while len(stones) >= 2:
            y = heapq.heappop(stones)
            heapq.heapify_max(stones)
            x = heapq.heappop(stones)

            # if they are not equal heappush the difference
            if x != y:
                diff = y - x
                heapq.heappush(stones, diff)
            heapq.heapify_max(stones)
            
        # return 
        print(stones)
        if stones:  
            return stones[0]
        else:
            return 0 

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna