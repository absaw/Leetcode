class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        '''
        dfs tree from (0,0) to (m-1,n-1)
        dp[(r,c)] = count the number of ways to reach destination from here

        subproblem; at each point in array, there are 2 possible paths, down and right
        dfs(r,c)
        '''

        ways = 0
        memo = {}
        def dfs(r,c):
            if (r,c) == (m-1,n-1):
                return 1
            if (r<0 or r>=m or c<0 or c>=n):
                return 0
            if (r,c) in memo:
                return memo[(r,c)]
            ways = dfs(r+1,c) + dfs(r,c+1)
            memo[(r,c)] = ways
            return ways
        
        return dfs(0,0)
