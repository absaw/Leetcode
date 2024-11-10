'''
amount = 7
coins = [1,3,4,5]
o/p: 2
Greedy: Doesn't work for case, 5+1+1 = 7 but ans is 3+4=7 i.e. 2
DFS with back tracking:Top Down:At each point you have 4 options to choose from. So a tree is made. But there is room for memoization.
Bottom Up:dp[amount]: If the amount to be covered is 0, dp[0] = 0
if a = 1, dp[1] = 1, i.e. taking coin 1, 1 time
dp[2] = 2, 1 coins : min 2 coins needed, i.e. 1 coin + dp[1] = 2
dp[3] = 1
dp[4] = 1
dp[5] = 1
dp[6] = 1+dp[5]=2 or dp[2] + dp[4]=3 or dp[3] + dp[3]=2
dp[7] = 1 + dp[6] = 3 or dp[3] + dp[4] = 2, dp[5] + dp[2] = 3 :: min = 2

So to pick the min soln, I have to find all the possible solutions. So a for loop over all the coins is needed. Keeping current coin in focus, coin =4, the other val needed would be 3, so dp[3], min(dp[coin],1+dp[amount-coint]);
'''

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        nCoinsNeeded = [amount+1] * (amount+1)
        nCoinsNeeded[0] = 0
        for currAmount in range(amount+1):
            for denomination in coins:
                # denomination: 1
                # currAmount: 7
                if denomination <= currAmount:
                    deficit = currAmount-denomination
                    nCoinsNeeded[currAmount] = min(nCoinsNeeded[currAmount],1+nCoinsNeeded[deficit])
        
        return nCoinsNeeded[amount] if nCoinsNeeded[amount]!=amount+1 else -1
                


