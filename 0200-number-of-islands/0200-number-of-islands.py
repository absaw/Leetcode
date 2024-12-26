class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # visited = set()
        m = len(grid)
        n = len(grid[0])
        def dfs(r,c):
            if (r<0 or c<0 or r>=m or c >= n or 
                grid[r][c]==-1 or grid[r][c]=="0"):
                return
            
            grid[r][c] = -1

            #visit neighbors
            dfs(r-1,c)
            dfs(r+1,c)
            dfs(r,c+1)
            dfs(r,c-1)
        nIslands = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c]=="1":
                    dfs(r,c)
                    nIslands += 1
        return nIslands