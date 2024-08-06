import collections
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])

        q = collections.deque()
        visited = set()
        total_oranges = 0
        rotten_oranges = 0
        fresh_oranges = 0
        def add_to_q(r,c):

            if ( r not in range(m) or
                 c not in range(n) or
                 (r,c) in visited or 
                 grid[r][c]!=1 ):
                 return
            q.append((r,c))
            visited.add((r,c))

        for r in range(m):
            for c in range(n):
                if grid[r][c]==0:
                    continue
                elif grid[r][c] == 2:
                    q.append((r,c))
                    visited.add((r,c))
                elif grid[r][c]==1:
                    fresh_oranges +=1 
                total_oranges += 1
        if fresh_oranges == 0:
            return 0

        minutes = 0
        while q:

            for i in range(len(q)):
                r,c = q.popleft()
                grid[r][c] = 2
                rotten_oranges += 1

                add_to_q(r-1,c)
                add_to_q(r+1,c)
                add_to_q(r,c-1)
                add_to_q(r,c+1)
               
            minutes += 1
        
        return minutes-1 if rotten_oranges == total_oranges else -1

