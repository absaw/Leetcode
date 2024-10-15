class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        high_p = low_p = prices[0]

        for i in range(1,len(prices)):
            
            if prices[i]< low_p:
                low_p = prices[i]
                high_p = prices[i]
            
            if prices[i] > high_p:
                high_p = prices[i]
                max_profit = max(max_profit,high_p - low_p)

        return max_profit	