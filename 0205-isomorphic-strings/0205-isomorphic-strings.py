class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        d = {}

        for i,c in enumerate(s):
            
            if c not in d:
                if t[i] in d.values():
                    return False
                d[c] = t[i]
            
            else:
                if d[c] != t[i]:
                    return False
        
        return True