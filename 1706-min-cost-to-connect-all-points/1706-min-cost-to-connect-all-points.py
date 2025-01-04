class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        #label for each point is 0-indexed from 0 to n-1
        adjList = collections.defaultdict(list) # (x,y): [(edge_length, neighbor)]
        N = len(points)
        for i in range(N):
            x1,y1 = points[i]
            for j in range(i+1,N):
                x2,y2 = points[j]

                cost = abs(y2-y1) + abs(x2-x1)
                adjList[i].append((cost,j))
                adjList[j].append((cost,i))
        
        #prim's
        visited=set()
        minHeap = [(0,0)] #(cost, point)
        minCost = 0
        
        while minHeap:
            
            cost, point = heapq.heappop(minHeap)

            if point in visited:
                continue
            
            minCost += cost
            visited.add(point)

            # add all neigboring edges to heap

            for edge_length, neighbor in adjList[point]:
                if neighbor not in visited:
                    heapq.heappush(minHeap,(edge_length,neighbor))
            
        return minCost

