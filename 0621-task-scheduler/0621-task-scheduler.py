from collections import Counter
import heapq
from collections import deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # establish data structures and variables
        heap = []
        queue = deque()
        time = 0 
        count = Counter(tasks)

        # turn dictionary into a max heap of tuples 
        for task, freq in count.items():
            heap.append((-freq, task))
        heapq.heapify(heap)
        print(heap)

        # count up the time while theres still stuff in the heap or queue
        while heap or queue:
            if heap:
                time += 1
                freq, task = heapq.heappop(heap)
                available_at = time + n
                print((freq, task, available_at))
                if freq + 1 < 0:
                    queue.append((freq + 1, task, available_at))
            elif queue[0][2] > time:
                time += 1  # idle, just increment
            if queue and queue[0][2] <= time:
                freq, task, available_at = queue.popleft()
                if freq < 0:
                    heapq.heappush(heap, (freq, task))
        return time

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna