class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        '''
        coins = 1,2,5
        amount = 11
        coins[0] = 0
        coins[1] = 1
        coins[2] = 1
        coins[3] = min(coins[1]+coins[2])
        coins[4] = min(coins[2]+coins[2]+coins[1]+coins[3])
        coins[5] = 1+coins[4] or coins[2]+coins[3]
        coins[6] = coins[1]+coins[5] or coins[2]+coins[4] or coins[3]+coins[3]
        code::
        coins = [0,0,0,0,0,0,0,0,0,0]
        '''
        dp = [amount+1]*(amount+1)
        dp[0] = 0
        for i in range(amount+1):
            for denom in coins:
                if denom<=i:
                    dp[i] = min(1+dp[i-denom],dp[i])
        
        return dp[amount] if dp[amount]<=amount else -1
              
    
