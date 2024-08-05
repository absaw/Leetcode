class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        

        max_area = 0

        m = len(grid)
        n = len(grid[0])

        visited = set()

        def dfs(r,c):

            if ( r not in range(m) or
                 c not in range(n) or
                 (r,c) in visited or 
                 grid[r][c] == 0):
                 return 0
            area = 0
            visited.add((r,c))
            directions = [(-1,0),(1,0),(0,1),(0,-1)]
            for d_r, d_c in directions:
                n_r = r + d_r
                n_c = c + d_c
                area += dfs(n_r,n_c)
            return 1 + area

        for r in range(m):
            for c in range(n):

                if grid[r][c] == 1 and (r,c) not in visited:

                    area = dfs(r,c)
                    max_area = max(area,max_area)
        
        return max_area
