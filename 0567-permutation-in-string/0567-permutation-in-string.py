class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1dict = {}
        s2dict = {}
        if len(s1)>len(s2):
            return False
        for ch in s1:
            s1dict[ch] = 1 + s1dict.get(ch,0)
        winLen = len(s1)
        l = 0
        for r in range(len(s2)):
            ch_r = s2[r]
            s2dict[ch_r] = 1 + s2dict.get(ch_r,0)

            if r >= winLen:
                ch_l = s2[l]
                s2dict[ch_l] -= 1
                if s2dict[ch_l]==0:
                    del s2dict[ch_l]
                l += 1
            if s2dict == s1dict:
                return True
            
        return False