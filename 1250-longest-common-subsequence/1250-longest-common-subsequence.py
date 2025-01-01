class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        '''
        abcde
           a   c   e 
        a  1   1   2
 t1     b  1   1   2
        c  1   2   2
        d  1   2   2
        e  1   2   3
        '''
        l1 = len(text1)
        l2 = len(text2)
        memo = [[0 for i in range(l2+1)] for j in range(l1+1)]
        # print(memo)
        for r in range(l1-1, -1, -1):
            for c in range(l2-1, -1, -1):
                if text1[r] == text2[c]:
                    memo[r][c] = memo[r+1][c+1] + 1
                else:
                    memo[r][c] = max(memo[r+1][c], memo[r][c+1])
                
        return memo[0][0]

