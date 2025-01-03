class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}
        def dfs(i,currSum):
            if i==len(nums):
                if currSum == target:
                    return 1
                else:
                    return 0

            
            if (i,currSum) in dp:
                return dp[(i,currSum)] 
            
            ways = 0

            ways = dfs(i+1, currSum +nums[i]) +dfs(i+1, currSum-nums[i])

            dp[(i,currSum)] = ways

            return ways

        return dfs(0,0)