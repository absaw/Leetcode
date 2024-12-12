class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2)<len(s1):
            return False
        
        s1Arr = [0] * 26
        s2Arr = [0] * 26

        for ch in s1:
            s1Arr[ord(ch)-ord('a')] += 1

        win = len(s1)
        l = 0
        for r in range(len(s2)):
            rch = s2[r]
            s2Arr[ord(rch)-ord('a')] += 1
            if r >= win:
                lch = s2[l]
                s2Arr[ord(lch)-ord('a')] -= 1
                l += 1
            if s1Arr == s2Arr:
                return True
        return False
