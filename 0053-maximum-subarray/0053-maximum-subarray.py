class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
       
        currSum = 0
        maxSum = float('-inf')
        for n in nums:
            if currSum<0:
                currSum = 0
            currSum += n
            maxSum = max(currSum,maxSum)
        
        return maxSum