class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        '''
        if word1[i] == word2[j]: ops = dfs(i+1,j+1)
        else:
            insert : ops1 =1+ dfs(i,j+1)
            delete: ops2 = 1+ dfs(i+1,j)
            replace: ops2  = 1+dfs(i+1,j+1)
            ops = min(op1,ops2,ops3)
        base case:
            i == len(word1):
                return len(word2) - j
            j == len(word2):
                return len(word1) - i
            
        '''
        dp = {}
        m = len(word1)
        n = len(word2)
        # if m == 0 
        def dfs(i,j):
            if i == m:
                return n-j
            if j == n:
                return m-i
            
            if (i,j) in dp:
                return dp[(i,j)]
            ops = 0
            if word1[i]==word2[j]:
                ops = dfs(i+1,j+1)
            else:
                ops = min(1+dfs(i,j+1), 1+ dfs(i+1,j), 1+dfs(i+1,j+1))
            dp[(i,j)] = ops
            return ops
        return dfs(0,0)