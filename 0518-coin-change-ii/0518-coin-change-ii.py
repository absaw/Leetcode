class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        '''
        recursion subproblem: with given i, currSum, in how many ways cna i reach the
        amount
        param(i, currSum)
        basecase : i>=len(coins) return 0
        currSum == amount: return 1
        currSum >amount return 0

        '''
        memo = {}

        def dfs(i, currSum):

            if i>=len(coins) or currSum>amount:
                return 0
            
            if currSum == amount:
                return 1
            
            if (i,currSum) in memo:
                return memo[(i,currSum)]
            
            # solve

            ways = 0

            ways = dfs(i, currSum+coins[i]) + dfs(i+1,currSum)

            memo[(i,currSum)] = ways

            return ways
        
        return dfs(0,0)