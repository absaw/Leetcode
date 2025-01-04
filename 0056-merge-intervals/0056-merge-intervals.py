class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])
        nS, nE = intervals[0]
        res = []
        for cS, cE in intervals:
            if nE<cS:
                res.append([nS,nE])
                nS, nE = cS, cE
            elif (cS<=nS<=cE or cS<=nE<=cE):
                nS = min(nS, cS)
                nE = max(nE, cE)

            elif (nS>cE):
                res.append([cS,cE])
            
        res.append([nS,nE])
        return res
