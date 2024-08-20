class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s

        #even
        l=0
        r=1
        n = len(s)
        max_s = ""
        max_len = 0
        for i in range(n-1):
            l = i
            r = i+1

            while (0 <= l < r < n) and s[l] == s[r]:
                currLen = r - l + 1
                if currLen > max_len:
                    max_len = currLen
                    max_s = s[l:r+1]
                l -= 1
                r += 1
        #odd 
        for i in range(0,n):
            l = i
            r = i
            while (0<=l <= r < n) and s[l]==s[r]:
                currLen = r-l + 1
                if currLen > max_len:
                    max_len = currLen
                    max_s = s[l:r+1]
                l -= 1
                r += 1
        
        return max_s