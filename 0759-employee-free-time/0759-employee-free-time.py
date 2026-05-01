"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""
class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        schedule2 = []
        for x in schedule:
            for y in x:
                schedule2.append([y.start, y.end])
        schedule2.sort(key = lambda x: x[0])
        start, end = schedule2[0][0], schedule2[0][1]
        res = []
        for i in range(1, len(schedule2)):
            if schedule2[i][0] <= end:
                end = max(end, schedule2[i][1])
            else:
                res.append([start, end])
                start, end = schedule2[i][0], schedule2[i][1]
        res.append([start, end])
        ans = []
        for i in range(len(res)-1):
            ans.append(Interval(res[i][1], res[i+1][0]))
        return ans