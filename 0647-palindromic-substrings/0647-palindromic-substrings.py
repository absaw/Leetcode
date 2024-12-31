class Solution:
    def countSubstrings(self, s: str) -> int:
        nPall = 0
        n = len(s)
        for i in range(n):
            #odd
            l = i
            r = i

            while l>=0 and r<n and s[l]==s[r]:
                nPall+=1
                l-=1
                r+=1
        for i in range(n-1):
            #even
            l = i
            r = i+1
            while l>=0 and r<n and s[l]==s[r]:
                nPall+=1
                l-=1
                r += 1
        return nPall