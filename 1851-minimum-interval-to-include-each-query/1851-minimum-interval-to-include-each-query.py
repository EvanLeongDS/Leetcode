import heapq
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # establish the return list, pre-sized so we can place answers by original index
        smallest_intervals = [0] * len(queries)
        # establish fundamental data structures
        heap = []
        heapq.heapify(heap)
        intervals.sort(key = lambda x: x[0])
        sorted_indices = sorted(range(len(queries)), key = lambda idx: queries[idx])
        i = 0

        # iterate while using a pointer
        for idx in sorted_indices:
            query = queries[idx]
            while i < len(intervals) and intervals[i][0] <= query:
                end = intervals[i][1]
                size = intervals[i][1] - intervals[i][0] + 1
                heapq.heappush(heap, (size, end))
                i += 1
            # pop the heap
            while heap and heap[0][1] < query:
                heapq.heappop(heap)

            if not heap:
                smallest_intervals[idx] = -1
            else:
                size, end = heap[0]
                smallest_intervals[idx] = size
        return smallest_intervals

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna