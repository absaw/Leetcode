class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        adjList = {i:[] for i in range(1,n+1)}
        
        for u,v,w in times:
            adjList[u].append([v,w])
        
        minHeap = [[0,k]]
        visited = set()
        # visited.add(k)
        minTime = 0
        while minHeap:

            dist, node = heapq.heappop(minHeap)
            if node in visited:
                continue
            minTime = max(minTime, dist)
            visited.add(node)
            # add neighbors to heap
            for neighbor, edge in adjList[node]:
                if neighbor not in visited:
                    heapq.heappush(minHeap,[dist+edge,neighbor])
            if len(visited)==n:
                return minTime
        return -1
