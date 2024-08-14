class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s)>len(t):
            return False
        elif len(s)==len(t):
            if s==t:
                return True
            else:
                return False
        p1 = 0
        p2 = 0

        while p1<len(s) and p2<len(t):
            
            if s[p1] == t[p2]:
                p1 += 1
            
            p2 += 1
        # print(p1)
        # print(p2)
        if p1 == len(s):
            return True
        
        return False

