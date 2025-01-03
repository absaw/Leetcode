class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        recursion: at each point i, i can either buy/cooldown, sell/cooldown
        subproblem: from given point, i , what is the max profit that can be generated
        buy: curr - prices[i] : dfs(i+1,)
        cool

        sell: curr+prices[i]
        cool
        param: i, currProfit, canBuy
        base case: i>= len (prices) : maxProfit = 0
        '''
        dp = {}

        def dfs(i, canBuy):

            if i>=len(prices):
                return 0
            
            if (i,canBuy) in dp:
                return dp[(i,canBuy)]
            maxP =0
            if canBuy:
                maxP =max(dfs(i+1,False) - prices[i] , dfs(i+1,canBuy))
            else:
                maxP = max(dfs(i+2,True)+prices[i], dfs(i+1, canBuy))
            dp[(i,canBuy)] = maxP
            return maxP
        return dfs(0,True)