from collections import defaultdict
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d,e = defaultdict(),defaultdict()

        for i,j in zip(s,t):
            if ((i in d.keys() and d[i] != j) or
                (j in e.keys() and e[j] != i)):
                return False
            d[i] = j
            e[j] = i

        return True