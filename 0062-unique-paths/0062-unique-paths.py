class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}
        def dfs(r,c):
            if (r not in range(m) or 
                c not in range(n)):
                return 0
            if (r,c) == (m-1,n-1):
                return 1
            if (r,c) in memo:
                return memo[(r,c)]
            
            ways = dfs(r+1,c) +dfs(r,c+1)
            memo[(r,c)] = ways
            return ways
        return dfs(0,0)

