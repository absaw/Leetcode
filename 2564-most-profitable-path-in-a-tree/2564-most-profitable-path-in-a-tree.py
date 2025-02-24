class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        '''
        node bob to root:
            dijkstra to find the shortest path for bob
        root to leaves: dfs to simulate movement for all possible paths
        '''
        n = len(edges)+1
        adjList = {i:[] for i in range(n)}
        for a, b in edges:
            adjList[a].append(b)
            adjList[b].append(a)
        #path from bob to root
        nTime = {}
        def dfs(node, par, time):

            if node == 0:
                nTime[node]=time
                return True
            
            for nei in adjList[node]:
                if nei == par:
                    continue
                
                if dfs(nei, node, time+1):
                    nTime[node] = time
                    return True

            return False
        
        dfs(bob, -1, 0)

        # bfs to find  optimal path

        queue = deque()#node, par, time, profit
        queue.append((0,-1, 0, amount[0]))
        maxProfit = float('-inf')
        while queue:
            node, par, time, profit = queue.popleft()

            for nei in adjList[node]:
                if nei == par:
                    continue
                neiTime = time+1
                neiProfit = amount[nei]
                if nei in nTime:
                    if neiTime > nTime[nei]:
                        neiProfit = 0
                    elif neiTime == nTime[nei]:
                        neiProfit = neiProfit//2
                    
                queue.append((nei, node, time+1, profit+neiProfit))

                if len(adjList[nei])==1:
                    maxProfit = max(maxProfit, profit+neiProfit)
        
        return maxProfit



            


            

