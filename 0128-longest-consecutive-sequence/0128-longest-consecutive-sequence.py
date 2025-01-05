class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        maxSeq = 1

        nSet = set(nums)
        
        for n in nSet:
            if n-1 not in nSet:
                # look only at start of sequence elements
                currSeq = 1
                while n+currSeq in nSet:
                    currSeq += 1
                maxSeq = max(currSeq, maxSeq)
        
        return maxSeq
