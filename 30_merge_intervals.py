from typing import List


A = [[1,3],[2,6],[8,10],[15,18]]
# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @return a list of Interval
    def merge(self, intervals: List[Interval]) -> List[Interval]:
        if not intervals:
            return []
        intervals.sort(key=lambda x: x.start)
        res = [intervals[0]]
        for i in range(1, len(intervals)):
            if intervals[i].start <= res[-1].end:
                res[-1].end = max(res[-1].end, intervals[i].end)
            else:
                res.append(intervals[i])
        return res
       

print(merge_intervals(A))
# Output: [[1, 6], [8, 10], [15, 18]]

