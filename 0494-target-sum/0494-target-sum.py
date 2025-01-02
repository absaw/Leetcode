class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        '''
        [1, 1, 1, 1, 1]
         i
        at each point i, include positive number or negative current number
        subproblem: from point i, with current sum, what is the no. of ways that the target can
        be achieved
        dp state: (i, currSum)
        base case: 
        check at last:
            if i == len(nums)
                if currSum == target, return 1
                else, return 0
        recursion: 
        take pos: dfs(i+1, target+nums[i]), i+1 since at each i we need to take the number only once
        take neg: dfs(i+1, target-nums[i])
        add both

        '''
        memo = {}
        def dfs(i, currSum):
            if i >= len(nums):
                if currSum == target:
                    return 1
                else:
                    return 0
            if (i,currSum) in memo:
                return memo[(i,currSum)]
            
            ways = dfs(i+1, currSum+nums[i]) + dfs(i+1, currSum-nums[i])

            memo[(i,currSum)] = ways

            return ways
        
        return dfs(0,0)


