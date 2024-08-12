class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        m = len(heights)
        n = len(heights[0])
        pac = set()
        atl = set()

        def trav(r,c,visited,prevHeight):
            #dfs traversal
            if ( (r,c) in visited or 
                 r not in range(m) or 
                 c not in range(n) or
                 heights[r][c] < prevHeight ):
                 return
            visited.add((r,c))
        
            #traverse neighbors
            trav(r+1,c,visited,heights[r][c])
            trav(r-1,c,visited,heights[r][c])
            trav(r,c+1,visited,heights[r][c])
            trav(r,c-1,visited,heights[r][c])



        for r in range(m):
            trav(r,0,pac,heights[r][0])
            trav(r,n-1, atl,heights[r][n-1])

        for c in range(n):
            trav(0,c,pac,heights[0][c])
            trav(m-1,c,atl,heights[m-1][c])
        result=[]
        for r in range(m):
            for c in range(n):
                if (r,c) in pac and (r,c) in atl:
                    result.append([r,c])
        
        return result
