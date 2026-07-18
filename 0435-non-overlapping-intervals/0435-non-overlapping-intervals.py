class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        output = 0 
        intervals.sort(key=lambda x: x[1])
        last_end = intervals[0][1]
        for interval in intervals[1:]:
            # if the start is less than the end of the last one 
            if interval[0] >= last_end:
                #keep
                last_end = interval[1]
            else:
                intervals.remove(interval)
                output += 1
        return output

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna