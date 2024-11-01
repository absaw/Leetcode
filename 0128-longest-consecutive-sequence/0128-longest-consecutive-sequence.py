class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        maxSequence = 0
        for i, num in enumerate(nums):
            if num-1 not in numSet:
                sequence=0
                while nums[i]+sequence in numSet:
                    sequence += 1
                maxSequence = max(sequence,maxSequence)
        return maxSequence