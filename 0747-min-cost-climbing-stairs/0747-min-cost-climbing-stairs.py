class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # [10,15,20,0]
        #           n-1
        cost.append(0)

        n = len(cost)

        for i in range(n-3,-1,-1):
            cost[i] += min(cost[i+1],cost[i+2])
        return min(cost[0],cost[1])
