class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        numD = {}

        for i in range(len(nums)):
            if target-nums[i] in numD:
                return [i,numD[target-nums[i]]]
            numD[nums[i]] = i
        