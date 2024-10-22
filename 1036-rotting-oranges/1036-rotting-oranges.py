from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        m = len(grid)
        n = len(grid[0])
        fresh = 0
        fresh_marked = 0

        for r in range(m):
            for c in range(n):

                if grid[r][c]==1:
                    fresh += 1
                elif grid[r][c] == 2:
                    queue.append([(r,c),0])
        minute=0	
        neighbors = [[-1,0],[1,0],[0,1],[0,-1]]
        while fresh >0 and queue:
            
            node, minute = queue.popleft()
            r,c = node
            # print(grid[r][c])
            if minute>0 and grid[r][c]==1:
                fresh -= 1
            grid[r][c] = 2
            # neighbors
            for add_r,add_c in neighbors:
                new_r,new_c = r+add_r, c+add_c

                if (new_r in range(m) and 
                    new_c in range(n) and 
                    grid[new_r][new_c]==1):
                    # fresh_marked +=1
                    queue.append([(new_r,new_c),minute+1])
        # print(fresh)
        # print(fresh_marked)
        # print(minute)
        if fresh_marked == fresh:
            return minute
        else:
            return -1