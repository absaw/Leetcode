class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        M = len(grid)
        N = len(grid[0])
        queue = collections.deque()
        visited = set()
        self.nFresh =0
        for r in range(M):
            for c in range(N):
                if grid[r][c] == 1:
                    self.nFresh += 1
                elif grid[r][c] == 2:
                    queue.append((r,c))
                    visited.add((r,c))
        if self.nFresh == 0:
            return 0
        self.nMin = -1
        neighbors = [[0,1],[0,-1],[1,0],[-1,0]]
        # self.nRotten = 0
        while queue:
            # r, c = queue.popleft()
            qLen = len(queue)

            for _ in range(qLen):
                r, c = queue.popleft()
                grid[r][c] = 2
                #find neighbors and add them to the queue
                for dr, dc in neighbors:
                    nr,nc = dr+r, dc+c

                    if (nr in range(M) and 
                        nc in range(N) and 
                        (nr,nc) not in visited and
                        grid[nr][nc]==1):
                        self.nFresh -= 1
                        queue.append((nr,nc))
                        visited.add((nr,nc))
            self.nMin +=1
        if self.nFresh ==0:
            return self.nMin
        return -1
