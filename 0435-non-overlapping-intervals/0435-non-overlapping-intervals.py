'''
1 - 2 - 3 - 4
1-------3
[1,2],[1,3],[2,3],[3,4],
========
1 - 2
1 - 2
1 - 2
=====
'''
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort(key = lambda x: x[0])
        prevEnd = intervals[0][1]
        eraseCount = 0
        for currStart, currEnd in intervals[1:]:
            # 1   -     7  8 - 9
            #   2 - 6
            if currStart >= prevEnd:
                prevEnd = currEnd
            else:
                eraseCount += 1
                prevEnd = min(prevEnd,currEnd)
        
        return eraseCount

