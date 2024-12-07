# s = "abcabcbb"
#      l
#         r
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        charSet = set()
        maxLen = 0
        if not s:
            return 0
        
        while r<len(s):
            # if s[r] not in charSet:
            #     charSet.add(s[r])
            #     r+=1
            if s[r] in charSet:
                while s[r] in charSet and l<r:
                    charSet.remove(s[l])
                    l += 1
            charSet.add(s[r])
            maxLen = max(maxLen,r-l+1)
            r+=1
                    
        return maxLen