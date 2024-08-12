class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) >len(s2):
            return False

        s1_d = {}
        s2_d = {}

        for i in range(97,123):
            s1_d[chr(i)] = 0
            s2_d[chr(i)] = 0
        
        for i in range(len(s1)):
            s1_d[s1[i]] += 1
            s2_d[s2[i]] += 1
        
        l = 0
        r = len(s1) - 1
        # print(s1_d)
        # print(s2_d)
        # print(s1_d)
        # print(s2[r-1])
        if s1_d == s2_d:
            return True
        while r < len(s2)-1 :
            r += 1
            s2_d[s2[r]] += 1
            s2_d[s2[l]] -= 1
            l += 1
            if s1_d == s2_d:
                return True
        return False
