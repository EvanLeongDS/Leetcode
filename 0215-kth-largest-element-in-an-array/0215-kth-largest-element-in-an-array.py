import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        my_heap = []
        heapq.heapify(my_heap)
        for num in nums:
            if len(my_heap) < k:
                heapq.heappush(my_heap, num)
            elif num > my_heap[0]:
                heapq.heappop(my_heap)
                heapq.heappush(my_heap, num)
        return my_heap[0]

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna