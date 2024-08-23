class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        min_p = max_p = prices[0]

        # profit = 0
        max_profit = 0
        for i in range(1,len(prices)):

            if min_p > prices[i]:
                min_p = prices[i]
                max_p= prices[i]
            if max_p < prices[i]:
                max_p = prices[i]
            profit = max_p-min_p

            max_profit = max(profit,max_profit)
        
        return max_profit