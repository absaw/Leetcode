class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        memo = {}

        def dfs(i, currSum):
            if currSum == amount:
                return 1
            
            #invalid case
            if i >= len(coins) or currSum > amount:
                return 0
            
            if (i,currSum) in memo:
                return memo[(i,currSum)]
            
            ways = dfs(i, currSum + coins[i]) + dfs(i+1, currSum)

            memo[(i,currSum)] = ways

            return ways
        
        return dfs(0,0)