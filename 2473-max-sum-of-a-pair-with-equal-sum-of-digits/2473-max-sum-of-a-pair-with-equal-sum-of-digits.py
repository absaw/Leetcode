class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        '''
        [18,   36,      27, 45]
        [9, 7, 9, 4, 7, 9, 9]
        digitSum: indices [0,2,5,6] 
        s = 9
        digitSum : maxHeap[54, 36]
        '''
        
        digitDict = {}
        # digitSum = []
        def getSum(n):
            s = 0
            while n:
                s += n%10
                n = n//10
            return s
        for n in nums:
            s = getSum(n)
            if s not in digitDict:
                digitDict[s] = []
            heapq.heappush(digitDict[s],n)
            if len(digitDict[s])>2:
                heapq.heappop(digitDict[s])
        
        #calc maxSum
        maxSum = -1
        for sums in digitDict.values():
            if len(sums)>1:
                curr = heapq.heappop(sums)
                curr += heapq.heappop(sums)
                maxSum = max(curr,maxSum)
        
        return maxSum
            
        

        


