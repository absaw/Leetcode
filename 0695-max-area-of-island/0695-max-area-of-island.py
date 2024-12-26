class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.maxArea = 0
        M = len(grid)
        N = len(grid[0])
        def dfs(r,c):

            if (r not in range(M) or
                c not in range(N) or  
                grid[r][c] == -1 or grid[r][c]==0):
                return 0 
            grid[r][c] = -1
            area = 1
            area += dfs(r,c+1)
            area += dfs(r,c-1)
            area += dfs(r+1,c)
            area += dfs(r-1,c)
            return area


        for r in range(M):
            for c in range(N):
                if grid[r][c]==1:
                    self.maxArea = max(self.maxArea,dfs(r,c))

        return self.maxArea