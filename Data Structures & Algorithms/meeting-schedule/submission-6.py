"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals)<2:
            return True
        intervals = sorted(intervals, key = lambda x:x.start)
        m = intervals[0].end
        print(m)
        for i in range(1, len(intervals)):
            if intervals[i].start < m:
                return False
            m = intervals[i].end
        return True

                