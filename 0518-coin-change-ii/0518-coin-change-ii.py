class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = {}
        def dfs(i, currSum):
            if currSum==amount:
                return 1
            if i>=len(coins) or currSum > amount:
                return 0
            if (i,currSum) in dp:
                return dp[(i,currSum)]
            
            # pick this coin
            ways=dfs(i, currSum+coins[i])
            #don't pick this coin
            ways += dfs(i+1, currSum)
            dp[(i,currSum)] = ways
            return ways
        return dfs(0, 0)

