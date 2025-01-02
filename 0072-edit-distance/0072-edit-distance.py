class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        '''
        recursion: no. of operations required from any particular pair of indices
        w1 = horse
             i
        w2 = ros
             j
        3 possibilites
        if w1[i] == w2[j], nOperations stays same
        else
            nOp += 1
            insert
            i stays same, j += 1
            replace
            i+=1, j+= 1
            remove
            i+=1, j same
        dp = (i,j)  - nOperations from this point
        '''

        memo = {}

        def dfs(i,j):

            if i == len(word1):
                return len(word2)-j
            if j==len(word2):
                return len(word1)-i
            # if (i>=len(word1) and j<len(word2)) or (i<len(word1) and j>=len(word2)):
            #     return 1

            
            if (i,j) in memo:
                return memo[(i,j)]
            nOperations = float('inf')
            if word1[i] == word2[j]:
                nOperations = dfs(i+1,j+1)
            else:
                # insert,
                nOperations = min(1+dfs(i,j+1),1+dfs(i+1,j), 1+dfs(i+1,j+1))

            memo[(i,j)] = nOperations
            return nOperations
        return dfs(0,0)