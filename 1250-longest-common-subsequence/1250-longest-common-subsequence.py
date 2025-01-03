class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        '''
        abcde
        i
        xefacewwi
        j
        lcs = ace
        if text1[i] == text2[j]: lcs = 1 + dfs(i+1,j+1)
        else: lsc = max(dfs(i+1,j), dfs(i,j+1))
        base case:
            if i>len(text1) or j>len(text2): return 0
        dp state: (i,j) : longest common subs from here
        '''

        dp = {}

        def dfs(i,j):
            if i>=len(text1) or j>=len(text2):
                return 0
            
            if (i,j) in dp:
                return dp[(i,j)]
            lcs = 0
            #compute
            if text1[i] == text2[j]:
                lcs = 1 + dfs(i+1,j+1)
            else:
                lcs = max(dfs(i+1,j),dfs(i,j+1))
            dp[(i,j)] = lcs
            return lcs
        return dfs(0,0)
        