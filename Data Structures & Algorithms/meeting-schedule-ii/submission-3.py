"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals) == 0:
            return 0

        starts = sorted(i.start for i in intervals)
        ends = sorted(i.end for i in intervals)

        start_ptr = 0
        end_ptr = 0
        rooms_now = 0
        output = 0  # tracks max rooms

        while start_ptr < len(starts):
            if starts[start_ptr] < ends[end_ptr]:  # condition: does a new meeting start before the earliest one ends?
                rooms_now += 1
                output = max(output, rooms_now)
                start_ptr += 1
            else:
                rooms_now -= 1
                end_ptr += 1

        return output
     
