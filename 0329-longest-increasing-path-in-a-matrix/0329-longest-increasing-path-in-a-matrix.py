class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dp = {}
        M = len(matrix)
        N = len(matrix[0])
        n = [[1,0],[-1,0],[0,1],[0,-1]]
        def dfs(r,c):
            
            if (r,c) in dp:
                return dp[(r,c)]
            longestPath = 1
            # neighbors
            for dr, dc in n:
                nr, nc = dr+r, dc+c
                if (nr not in range(M) or 
                    nc not in range(N) or
                    matrix[r][c]>=matrix[nr][nc]):
                    continue
                longestPath = max(longestPath, 1+dfs(nr,nc))
            dp[(r,c)] = longestPath
            return longestPath
        for r in range(M):
            for c in range(N):
                dfs(r,c)
        return max(dp.values())
                