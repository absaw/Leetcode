class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        m = len(grid)
        n = len(grid[0])
        def dfs(r,c):
            
            if (r not in range(m) or
                c not in range(n) or 
                # (r,c) in visited or 
                grid[r][c] != "1"):
                return 
            
            grid[r][c] = "3"
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)

        nIslands = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == "1":
                    dfs(r,c)
                    nIslands += 1
                    
        return nIslands
