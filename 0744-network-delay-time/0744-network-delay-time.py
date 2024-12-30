'''
Dijstra's algo
Basically weighted bfs. But instead of a queue, I am using minHeap, to maintain the 
nodes to visit next. at each point i pop the min weight neighbor
if node already visited, then continue
add it to visited.
update times value to be max
Then update the weights of all neighbors of this node

'''
import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        # create adj List 
        adjList = collections.defaultdict(list)

        for u, v, w in times:
            adjList[u].append((v,w))
        # 1:(1,2)
        minHeap = [(0,k)]
        visited = set()
        heapq.heapify(minHeap)
        res = 0
        while minHeap:

            weight, node = heapq.heappop(minHeap)
            if node in visited:
                continue
            
            visited.add(node)
            res = max(res,weight)
            # traverse through neighbors and update the weights

            for neighbor, n_weight in adjList[node]:
                if neighbor not in visited:
                    heapq.heappush(minHeap,(n_weight+weight, neighbor))
            
        return res if len(visited) == n else -1


        

