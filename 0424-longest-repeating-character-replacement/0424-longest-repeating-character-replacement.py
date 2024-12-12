'''
ABCAAADA
 ^^
k = 1
no. of replacements needed = winLength - max frequency character in all
for eg.
AAAAABAB
L      R
A = 5
B = 1
k=3
nreplacements = 8-6 = 2
so 2 Bs can be replaced
'''
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        chArr = [0]*26
        l = r = 0
        lSub = 0
        while r < len(s):
            winLen = r-l+1
            ich = ord(s[r])-ord('A')
            chArr[ich]+=1
            mfchar = max(chArr)
            
            nReplacement = winLen - mfchar
            if nReplacement <= k:
                lSub = max(lSub,winLen)
            else:
                i_ch = ord(s[l])-ord('A')
                chArr[i_ch]-=1
                l += 1
                
            r +=1
        return lSub
                
