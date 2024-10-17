class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key=lambda x: x[0])
        curr = intervals[0]
        res = []
        for i in range(1,len(intervals)):
            l, r = intervals[i]
            
            if l <= curr[1] and r>curr[1]:
                curr[1] = r
            elif l>curr[1]:
                res.append(curr)
                curr = intervals[i]
        if curr:
            res.append(curr)
        return res