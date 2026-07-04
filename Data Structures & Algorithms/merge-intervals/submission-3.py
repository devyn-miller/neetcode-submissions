class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals)==1:
            return intervals
        intervals = sorted(intervals, key = lambda x: x[0])
        print(intervals)
        re = []
        curr_min, curr_max = intervals[0][0], intervals[0][1]
        for i in range(1, len(intervals)):
            print(curr_min, curr_max)
            if intervals[i][0] <= curr_max:
                curr_max = max(intervals[i][1], curr_max)
                if i == len(intervals) - 1:
                    re.append([curr_min, curr_max])
            else:
                re.append([curr_min, curr_max])
                curr_min, curr_max = intervals[i][0], intervals[i][1]
                if i == len(intervals) - 1:
                    re.append([curr_min, curr_max])
        return re
