class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        '''
        at each point i can select from range(i,n) coins to select
        to make up the amount
        subproblem: given index i, what is the min no. of coins that can
        be taken to make up the amount
        parameters: currAmt/remAmt
        dp state: (currAmt)
        choices:
        for i in range(i,len(coins)):
            if currAmt+coins[i]<amount:
                minCoins = min(minCoins, dfs(i+1, currAmt+coins[i]))
        base case: currAmt = amount: minCoins = 0
        i>len(coins), minCoins
        i don't need to keep track of i, since that is taken care of by the for loop itself
        '''

        memo = {}

        def dfs(currAmt):
            if currAmt == amount:
                return 0

            if currAmt in memo:
                return memo[currAmt]
                
            # pick coin
            nCoins = float('inf')
            for j in range(len(coins)):
                if currAmt + coins[j] <= amount:
                    nCoins = min(nCoins, 1+dfs(currAmt+coins[j]))
                
            memo[currAmt] = nCoins

            return nCoins
        minC= dfs(0)
        return minC if minC!=float('inf') else -1