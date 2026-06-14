import math
import heapq 
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        my_heap = []
        heapq.heapify(my_heap)
        for point in points:
            x, y = point[0], point[1]
            distance = math.sqrt(x**2 + y**2)
            if len(my_heap) < k:
                heapq.heappush(my_heap, (-distance, point))

            elif -distance > my_heap[0][0]:
                heapq.heappop(my_heap)
                heapq.heappush(my_heap, (-distance, point))

        output = []
        for lebron in my_heap:
            output.append(lebron[1])
        return output

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna