class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        '''
        recursive function
        essentially i need to find a subarray which sums upto the half of the total sum
        at each step, i have the option of taking a number or not taking it
        this would result in a dfs tree
        i can memoize the parts of this tree
        '''
        # dp={10:True/false,11:True}
        dp = {}
        if sum(nums)%2 != 0:
            return False
        # 1, 5, 11, 5
        # ^
        # i
        def dfs(i, remSum):

            if remSum == 0:
                return True
            if i>=len(nums):
                return False

            if remSum < 0:
                return False
                # this branch doesn't  lead to the solution
            if (i,remSum) in dp:
                return dp[(i,remSum)]
            result = dfs(i+1, remSum) or dfs(i+1, remSum-nums[i])
            dp[(i,remSum)] = result
            return result
        
        return dfs(0, sum(nums)//2)
