class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])

        res = [[float('inf')] * (n+1) for i in range(m+1)]

        res[m][n-1] = 0

        for r in range(m-1,-1,-1):
            for c in range(n-1,-1,-1):

                res[r][c] = grid[r][c] + min(res[r+1][c],res[r][c+1])
        
        # print(res)

        return res[0][0]


