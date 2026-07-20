"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""


class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starts = sorted(list(x.start for x in intervals))
        ends = sorted(list(x.end for x in intervals))

        s = 0
        e = 0
        ct = 0
        m = 0
        while s < len(intervals) and e < len(intervals):
            if starts[s] < ends[e]:
                ct += 1
                s += 1
                
            else:
                e += 1
                ct -=1
            m = max(m, ct)
        return m
            