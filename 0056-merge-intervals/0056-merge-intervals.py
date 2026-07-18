class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # output[a,b] interval[c, d] a <=d c<=b overlap
        output = []
        intervals.sort(key=lambda x: x[0])
        for interval in intervals:
            # check for overlapping intervals 
            if len(output) == 0:
                output.append(interval)
            if len(output) > 0 and output[-1][0] <= interval[1] and interval[0] <= output[-1][1]:
                # we have an overlap!
                if interval[1] > output[-1][1]:
                    output[-1][1] = interval[1]
                if interval[0] < output[-1][0]:
                    output[-1][0] = interval[0]
            else:
                output.append(interval)
        return output
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna