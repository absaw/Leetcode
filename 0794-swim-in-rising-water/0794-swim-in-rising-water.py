class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        import heapq
        N = len(grid)

        visited = set() # (r,c)
        minHeap = [(grid[0][0],0,0)] # maxHeight, r, c
        heapq.heapify(minHeap)
        visited.add((0,0))
        neighbors = [[0,1],[0,-1],[1,0],[-1,0]]
        self.leastTime=0
        while minHeap:

            # pop element from heap and 
            currMaxH, r, c = heapq.heappop(minHeap)
            if (r,c) == (N-1,N-1):
                # nonlocal leastTime 
                self.leastTime = currMaxH
                break
            # add its neighbors to heap, add max(currMaxH, neighbor) to heap

            for dr, dc in neighbors:
                nr, nc = dr+r, dc+c
                if (0<=nr<N and 0<=nc<N and (nr,nc) not in visited):
                    visited.add((nr,nc))
                    heapq.heappush(minHeap,(max(currMaxH,grid[nr][nc]), nr, nc))
        return self.leastTime




