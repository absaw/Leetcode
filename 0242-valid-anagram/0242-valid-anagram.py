class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        l1 = [0] * 26
        l2 = [0] * 26
        for i in range(len(s)):
            ch1 = s[i]
            i_ch1 = ord(ch1) - ord('a')
            l1[i_ch1] += 1

            ch2 = t[i]
            i_ch2 = ord(ch2) - ord('a')
            l2[i_ch2] += 1
        
        return True if l1==l2 else False
            