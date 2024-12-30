'''
Min cost spanning tree is asked
Make adj list for each number, for all other points which can be its neighbors

Prim's algorithm which is simliar to dijstra. Maintain a minHeap to track the min next neighbor which can be visited.
add any element to the minHeap
start while loop
pop out element. If element is visited, then continue
add it to visited set. add the cost to result.
visit neighbors which are adjacent to the heap.

'''
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        # create the adj list for all pair of points

        N = len(points)

        adjList = collections.defaultdict(list)# cost, point_index

        for i in range(N):
            x1,y1 = points[i]
            for j in range(i+1,N):
                x2, y2 = points[j]
                cost = abs(y1-y2) + abs(x1-x2)

                adjList[i].append([cost,j])
                adjList[j].append([cost,i])
        
        # prim's algo
        import heapq
        visited = set()
        minHeap = [(0,0)] # cost, node
        totalCost = 0
        while minHeap:

            cost, node = heapq.heappop(minHeap)
            if node in visited:
                continue
            totalCost += cost
            visited.add(node)
            # neighbors

            for nCost, neighbor in adjList[node]:
                if neighbor not in visited:
                    heapq.heappush(minHeap, (nCost,neighbor))

        return totalCost