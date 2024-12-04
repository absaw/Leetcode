
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False
        s_arr = [0]*26
        t_arr = [0]*26

        for i in range(len(s)):
            ch_s= ord(s[i])-ord('a') 
            ch_t = ord(t[i])-ord('a')
            s_arr[ch_s] += 1
            t_arr[ch_t] += 1
        return s_arr==t_arr