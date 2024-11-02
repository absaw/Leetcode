class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        window = set()
        #window[s[l]] = 1+ window.get(s[l],0)
        maxLen = 0
        #  v 
        while r<len(s):
            
            if s[r] in window:
                while s[r] in window and l<r:
                    window.remove(s[l])
                    l+=1
            window.add(s[r])
            maxLen = max(maxLen, r-l+1)
            r += 1
        return maxLen