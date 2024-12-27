class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        
        self.maxScore = 0

        i = 0
        j = i+1

        self.maxI = values[i]
        self.maxScore = self.maxI + values[j]-j
        # self.maxJ = values[j] +j

        for j in range(1,len(values)-1):
            val2 = values[j+1]-(j+1)
            val1 = values[j]+j
            self.maxI = max(self.maxI,val1)
            self.maxScore = max(self.maxScore, self.maxI+val2)

        return self.maxScore
