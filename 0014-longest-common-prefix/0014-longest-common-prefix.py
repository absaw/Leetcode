class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        prefix = ""

        i = 0

        min_len = len(min(strs))

        while i < min_len:

            c = strs[0][i]
            for s in strs:
                if s[i] != c:
                    return prefix
            
            prefix += c
            i += 1
        
        return prefix