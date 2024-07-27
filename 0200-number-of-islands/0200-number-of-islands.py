class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        if not grid:
            return 0
        rows, cols = len(grid),len(grid[0])
        islands = 0
        # visited = [[0]*cols]*rows
        visited = set()
        # print(visited)
        def bfs(r,c):
            q = collections.deque()
            q.append((r,c))
            # visited[r][c] = 1
            visited.add((r,c))
            while(q):
                nr,nc = q.popleft()
                directions = [[0,1] , [1,0], [-1,0], [0,-1]]
                for dr, dc in directions:
                    neighbor_r = nr + dr
                    neighbor_c = nc + dc
                    # print(range(rows))
                    if (neighbor_r in range(rows) and
                        neighbor_c in range(cols) and
                        grid[neighbor_r][neighbor_c] == "1" and
                        (neighbor_r,neighbor_c) not in visited):
                        # visited[neighbor_r][neighbor_c] == 0):

                        # visited[neighbor_r][neighbor_c] = 1
                        visited.add((neighbor_r,neighbor_c))

                        q.append((neighbor_r,neighbor_c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    # visited[r][c] = 1
                    bfs(r,c)
                    islands += 1
                
        return islands