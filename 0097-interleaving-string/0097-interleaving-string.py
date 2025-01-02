class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        '''
        s1 = aabcc 
             i1
        s2 = dbbca
             i2
        s3 = aadbbbaccc
        3 cases:
        s3 matches s1 
        s3 matches s2
        s3 matches both s1 and s2
        recursion: for current i1, i2, can i obtain s3 : True/false
        def state : i1, i2
        base case: i1 ==len(s1) and i2 == len(s2), since we only move forward when we find one of the 3 cases

        '''
        if len(s1) + len(s2) != len(s3):
            return False
        dp = {}
        def canInterleave(i1, i2):
            # base case
            if i1 == len(s1) and i2 == len(s2):
                return True
            if (i1,i2) in dp:
                return dp[(i1,i2)]
            if i1 < len(s1) and s1[i1] == s3[i1+i2]:
                if canInterleave(i1+1,i2):
                    return True
            if i2<len(s2) and s2[i2] == s3[i1+i2]:
                if canInterleave(i1,i2+1):
                    return True
            
            dp[(i1,i2)] = False

            return False
        return canInterleave(0,0)