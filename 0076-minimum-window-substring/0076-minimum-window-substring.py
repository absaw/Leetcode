class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m = len(s)
        n = len(t)
        if m < n:
            return ""

        sdict, tdict = {}, {}
        for ch in t:
            tdict[ch] = 1+tdict.get(ch,0)
        l = 0
        have = 0
        need = len(tdict)
        res = [-1,-1]
        resLen = float('inf')
        for r in range(len(s)):
            ch = s[r]
            sdict[ch] = 1 + sdict.get(ch,0)

            if ch in tdict and sdict[ch]==tdict[ch]:
                have += 1
            
            while have == need:
                if r-l+1 < resLen:
                    res = [l,r]
                    resLen = r-l+1
                sdict[s[l]] -= 1
                if s[l] in tdict and sdict[s[l]] < tdict[s[l]]:
                    have -= 1
                l += 1
        return s[res[0]:res[1]+1] if resLen != float('inf') else ""
