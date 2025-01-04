class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        #bellman fords'

        prices = [float('inf')]*n
        prices[src] = 0
        for _ in range(k+1): #since k stops, k+1 edges till dest, so relaxing that many times
            tmpPrice = prices.copy()
            for src, dest, price in flights:
                if prices[src] == float('inf'):
                    continue
                
                if prices[src]+price < tmpPrice[dest]:
                    tmpPrice[dest] = prices[src] + price
            prices = tmpPrice
        
        return prices[dst] if prices[dst]!=float('inf') else -1
                
# class Solution:
#     def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
#         prices = [float('inf')]*n
#         prices[src] = 0

#         for i in range(k+1):
#             tmpPrice = prices.copy()
#             for s, d, p in flights:
#                 if prices[s] == float('inf'):
#                     continue
#                 if prices[s]+p < tmpPrice[d]:
#                     tmpPrice[d] = prices[s]+p
#             prices = tmpPrice
        
#         return prices[dst] if prices[dst]!=float('inf') else -1