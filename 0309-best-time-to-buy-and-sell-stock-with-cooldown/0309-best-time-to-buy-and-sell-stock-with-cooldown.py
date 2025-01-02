class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        at each point, i have 3 options
        buy, sell, cooldown
        essentially just 2 - buy and cool or sell and cool
        buy : dfs(i+1,sell) - prices[i]
        sell: dfs(i+2,buy) + prices[i]
        cooldown: dfs(i+1,sameAsBefore), profit remains same 
        cause I only can buy or sell at a time
        subproblem: at any particular point i in the array, what is the max
        profit that can be made
        base case - i >= len(prices) , maxProfit = 0
        defining state: i, wether can buy or sell at that point, cause that
        determines the decisions that can be taken
        '''
        dp = {}
        # maxProfit = 0
        def dfs(i, buying):

            if i>=len(prices):
                return 0

            if (i,buying) in dp:
                return dp[(i,buying)]
            maxProfit = 0
            if buying:
                buyProfit = dfs(i+1, False)-prices[i]
                cooldownProfit = dfs(i+1, buying)
                maxProfit = max(buyProfit, cooldownProfit)
            else:
                sellProfit = dfs(i+2, True)+prices[i]
                cooldownProfit = dfs(i+1, buying)
                maxProfit = max(sellProfit, cooldownProfit)
            dp[(i,buying)] = maxProfit
            return maxProfit
        # dfs(0, True)

        return dfs(0, True)