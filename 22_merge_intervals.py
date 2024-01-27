"""
Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

"""
from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x : x[0])
        res = [intervals.pop(0)]
        for i in intervals:
            if i[0] <= res[-1][1]:
                lst = res.pop()
                item = [min(lst[0],i[0]), max(lst[1],i[1])]
                res.append(item)
            else:
                res.append(i)
        return res

A = [[1,4],[2,3]]
print(Solution().merge(A))