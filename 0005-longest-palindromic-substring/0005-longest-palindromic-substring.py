class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        res = ""
        maxLen=0
        #odd length
        for i in range(len(s)):
            l = i
            r = i
            while(l>=0 and r<len(s) and s[l] == s[r]):
                if maxLen<(r-l+1):
                    res = s[l:r+1]
                    maxLen=r-l+1
                l -= 1
                r += 1
        #even length
        for i in range(len(s)-1):
            l = i
            r = i+1
            while(l>=0 and r<len(s) and s[l]==s[r]):
                if maxLen < (r-l+1):
                    res = s[l:r+1]
                    maxLen=r-l+1
                l -=1 	
                r +=1
        return res
