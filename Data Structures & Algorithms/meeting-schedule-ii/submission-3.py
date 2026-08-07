class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starts = sorted([i.start for i in intervals])
        ends = sorted([v.end for v in intervals])
        s, e = 0,0
        ct = 0
        m=0
        while s<len(intervals) and e<len(intervals):
            if starts[s]<ends[e]:
                s += 1
                ct += 1
            else:
                e += 1
                ct -= 1
            m = max(m, ct)
        return m