class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        maxS = 0
        for num in nums:
            if num-1 not in numSet:
                # calc max sequence
                currS = 1
                # n = num
                while num+currS in numSet:
                    currS += 1
                
                maxS = max(maxS,currS)

        return maxS    
                