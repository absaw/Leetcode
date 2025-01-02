class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        '''
        space optimized version
        '''

        currentRow = defaultdict(int)
        currentRow[0] = 1 # for getting sum 0, there is 1 way
        for i in range(len(nums)):
            nextRow = defaultdict(int)
            for currSum, ways in currentRow.items():
                nextRow[currSum+nums[i]] += ways
                nextRow[currSum-nums[i]] += ways
            currentRow = nextRow
        
        return currentRow[target]
