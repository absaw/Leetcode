class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = r = 0
        maxF = 0
        chArr = [0]*26
        lsub = 0
        while r < len(s):
            winLen = r-l+1
            chArr[ord(s[r])-ord('A')] += 1
            maxF = max(maxF, chArr[ord(s[r])-ord('A')])

            if winLen-maxF > k:
                chArr[ord(s[l])-ord('A')] -= 1
                l+=1
            else:
                lsub = max(lsub,winLen)
            r += 1
        return lsub