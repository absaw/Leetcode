class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        newStart,newEnd = newInterval
        i = 0
        res = []
        for currStart, currEnd in intervals:
            
            if newEnd < currStart:
                res.append([newStart,newEnd])
                res = res + intervals[i:]
                return res
            if newStart in range(currStart,currEnd+1) or newEnd in range(currStart,currEnd+1):
                newStart,newEnd = [min(currStart,newStart),max(currEnd,newEnd)]
            if newStart > currStart:
                res.append([currStart,currEnd])
            i += 1

        res.append([newStart,newEnd])
        return res
