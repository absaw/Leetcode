class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        
        maxSum = nums[0]
        currSum = nums[0]
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                currSum += nums[i]
            else:
                currSum = nums[i]
            maxSum = max(currSum,maxSum)
        
        return maxSum