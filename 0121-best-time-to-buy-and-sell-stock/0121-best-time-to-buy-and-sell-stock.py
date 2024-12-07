#     7, 1, 5, 3, 6, 4, 0, 8
# min 7  1              0
# max 7  1  5           0  8
# curP0  0  4  3  5  3  0  8
# maxP = 8
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        minPrice = prices[0]
        maxProfit = 0

        for i in range(1,len(prices)):

            if prices[i] < minPrice:
                minPrice = prices[i]
                # maxPrice = prices[i]
            else:
                if prices[i]-minPrice > maxProfit:
                    maxProfit = prices[i]-minPrice
        return maxProfit