class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        # adjMat = {src:[] for src,dest in tickets}
        # tickets.sort()

        # for src,dest in tickets:
        #     adjMat[src].append(dest)

        # res = ["JFK"]

        # def dfs(node):
        #     if len(res) == len(tickets)+1:
        #         return True
            
        #     if node not in adjMat:
        #         return False
        #     temp = list(adjMat[node])
        #     # traverse neighbors
        #     for i, neighbor in enumerate(temp):
        #         res.append(neighbor)
        #         adjMat[node].pop(i)

        #         if dfs(neighbor): return True

        #         res.pop()
        #         adjMat[node].insert(i,neighbor)
            
        #     return False
        
        # dfs("JFK")

        # return res
       
        adj = defaultdict(list)
        for src, dst in sorted(tickets):
            adj[src].append(dst)

        res = []
        def dfs(src):
            while adj[src]:
                dst = adj[src].pop(0)
                dfs(dst)
            res.append(src)
            
        dfs('JFK')
        return res[::-1]