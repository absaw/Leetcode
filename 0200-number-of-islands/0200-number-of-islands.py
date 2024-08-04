from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        n_island = 0
        m = len(grid)
        n = len(grid[0])

        visited = [ [0] * n for _ in range(m)]
        def bfs(r,c):
            q = deque()
            q.append([r,c])
            visited[r][c] = 1
            while q:
                i, j = q.popleft()
                visited[i][j] = 1
                neighbors = [(i+1,j),
                                (i-1,j),
                                (i,j+1),
                                (i,j-1)]
                
                for n_r,n_c in neighbors:
                    if (n_r in range(m) and
                        n_c in range(n) and
                        visited[n_r][n_c] == 0 and 
                        grid[n_r][n_c] =="1"):
                        q.append([n_r,n_c])
                        visited[n_r][n_c] = 1 # This makes all the difference since we aren't visting each neighbor now. 
        for r in range(m):
            for c in range(n):
                if visited[r][c] == 0 and grid[r][c] == "1":
                    n_island += 1
                    bfs(r,c)
                elif visited[r][c] == 0 and grid[r][c] == "0":
                    visited[r][c] = 1
                
        
        return n_island