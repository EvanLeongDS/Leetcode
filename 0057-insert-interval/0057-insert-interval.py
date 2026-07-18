class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # interval = [a, b], newInterval = [c, d] and a <= d and c <= b 
        output = [] # final return
        min_interval = newInterval[0]
        max_interval = newInterval[1]
        interval_output = [min_interval, max_interval]
        mergeAdded = False

        # iterate to find the overlapping interval and determine what goes in output 
        for interval in intervals:
            if interval[1] < min_interval:
                output.append(interval)
            if interval[0] <= max_interval and min_interval <= interval[1]:
                if interval[0] < min_interval:
                    min_interval = interval[0]
                    interval_output[0] = interval[0]
                if interval[1] > max_interval:
                    max_interval = interval[1]
                    interval_output[1] = interval[1]
            if interval[0] > max_interval and mergeAdded is False:
                output.append(interval_output)
                mergeAdded = True
            if interval[0] > max_interval:
                output.append(interval)

        if not mergeAdded:
            output.append(interval_output)
        return output


        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna