class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        #pacific ocean 
        visited_pacific = set()
        visited_atlantic = set()
        M = len(heights)
        N = len(heights[0])
        neighbors = [[0,1],[0,-1],[1,0],[-1,0]]
        def dfs(r,c,visited):
            # if (r not in range(M) or 
            #     c not in range(N) or
            #     (r,c) in visited):
            #     return
            visited.add((r,c))
            #explore the neighbors
            for dr, dc in neighbors:
                nr,nc = dr+r,dc+c

                if (nr in range(M) and 
                    nc in range(N) and
                    (nr,nc) not in visited and
                    heights[nr][nc]>=heights[r][c]):
                    dfs(nr,nc,visited)
        
        for c in range(N):
            #pacific row
            dfs(0,c,visited_pacific)
            #atlantic row
            dfs(M-1,c,visited_atlantic)
        for r in range(M):
            #pacific col
            dfs(r,0,visited_pacific)
            #atlantic col
            dfs(r,N-1,visited_atlantic)
        # print(visited_pacific)
        # print(visited_atlantic)
        ints = visited_pacific & visited_atlantic
        # print(ints)
        result = [[r,c] for r,c in list(ints)]
        return result



