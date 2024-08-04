from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        n_island = 0
        m = len(grid)
        n = len(grid[0])

        visited = [ [0] * n for _ in range(m)]

        for r in range(m):
            for c in range(n):
                # print("r,c =",r,c)
                # print(visited[r][c],grid[r][c])
                if visited[r][c] == 0 and grid[r][c] == "1":
                    # print(visited)
                    n_island += 1
                    # print('Count> r,c =',r,c)

                    #bfs traversal

                    q = deque()

                    q.append([r,c])
                    visited[r][c] = 1
                    while q:
                        i, j = q.popleft()
                        visited[i][j] = 1
                        # print("visited ",i,j)

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
                                visited[n_r][n_c] = 1
                        

                elif visited[r][c] == 0 and grid[r][c] == "0":
                    visited[r][c] = 1
                    # print("visited ",r,c)
                
        
        return n_island