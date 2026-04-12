"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda i : i.start)
        for i in range(1,len(intervals)):
            in1 = intervals[i-1].end
            in2 = intervals[i].start
            if in1 > in2 : return False
        return True