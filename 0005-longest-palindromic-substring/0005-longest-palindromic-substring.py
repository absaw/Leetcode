class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        n = len(s)
        for i in range(n):
            # odd length
            l = i
            r = i
            while l>=0 and r < n and s[l]==s[r]:
                if (r-l+1)>len(res):
                    res = s[l:r+1]
                l -= 1
                r += 1
        for i in range(n-1):
            l = i
            r = i+1
            while l>=0 and r<n and s[l]==s[r]:
                if (r-l+1)>len(res):
                    res = s[l:r+1]
                l-=1 
                r+=1

        return res
