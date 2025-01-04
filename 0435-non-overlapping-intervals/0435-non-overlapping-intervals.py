class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[0])

        prevEnd = intervals[0][1]
        count = 0
        for currS, currE in intervals[1:]:

            if prevEnd <=currS:
                prevEnd = currE
            
            elif prevEnd > currS:
                count += 1
                prevEnd = min(currE, prevEnd)
        
        return count