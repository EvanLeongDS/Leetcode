class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        # if interval[i][1] >= interval[i +1][0] merge it 
        # or if interval[0] <= interval[i+1][1]

        # base case 
        if not intervals:
            return []

        # sort the intervals and establish the new interval to return
        intervals.sort()
        new_intervals = []
        new_intervals.append(intervals[0])
        
        # go through the rest of intervals and see if they overlap with the most recent interval in new intervals
        # otherwise just append it 
        for i in range(1, len(intervals)):
            if intervals[i][0] <= new_intervals[-1][1]:
                new_intervals[-1][1] = max(new_intervals[-1][1], intervals[i][1])
            else:
                new_intervals.append(intervals[i])        
        return new_intervals
            
               
