import heapq
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # grab original indices sort tasks to get the tasks first to process
        #enqueueTime, processingTime, originalIndex
        for i in range(len(tasks)):
            tasks[i].append(i)
        tasks.sort()

        # establish fundamental variabiles
        curr_time = tasks[0][0] # gradually increment from processing time to the next enQueue time
        heap = [] # will be used for getting the smallest processing time 
        result = [] # will put indices in her

        # go through the tasks and use the heap to sort stuff out 
        i = 0 
        n = len(tasks)
        while i < n or heap:
            if not heap:
                curr_time = max(curr_time, tasks[i][0])
            while i < n and tasks[i][0] <= curr_time:
                heapq.heappush(heap, [tasks[i][1], tasks[i][2]])
                i += 1
            processing_time, original_index = heapq.heappop(heap)
            curr_time += processing_time
            result.append(original_index)
        return result

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna