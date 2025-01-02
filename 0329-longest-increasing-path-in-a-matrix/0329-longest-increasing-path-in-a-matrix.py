class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        '''
        recursive function: longest path: from this point r,c what is the longest path i can travel to

        base case: if can't traverse to any of the neighbors, return 0

        dp state, r,c : longest path that can be traversed from this point
        the next call would be only made if the val is increasing. So the possibility of revisiting a node vanishes with that check
        '''
        path=set()
        M = len(matrix)
        N = len(matrix[0])
        neighbors = [[0,1],[0,-1],[1,0],[-1,0]]
        memo = {}
        def dfs(r,c):

            # if (r not in range(M) or
            #     c not in range(N)):
            #     return 0
            if (r,c) in memo:
                return memo[(r,c)]
            #traverse to neighbors
            longestPath = 1
            for dr, dc in neighbors:
                nr, nc = dr+r, dc + c
                if (0<=nr<M and 0<=nc<N and 
                    matrix[nr][nc]>matrix[r][c]):
                    longestPath = max(longestPath,1+dfs(nr,nc))
            memo[(r,c)] = longestPath
            return longestPath
        lp = 0
        for r in range(M):
            for c in range(N):
                lp = max(lp,dfs(r,c))
        return lp