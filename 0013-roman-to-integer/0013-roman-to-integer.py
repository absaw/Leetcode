class Solution:
    def romanToInt(self, s: str) -> int:
        i = 0
        symDict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
            'IV': 4,
            'IX': 9,
            'XL': 40,
            'XC': 90,
            'CD': 400,
            'CM': 900,
        }

        num = 0
        while i < len(s):
            if (i+1 < len(s) and symDict[s[i+1]]>symDict[s[i]]):
                sym = s[i:i+2]
                num += symDict[sym]
                i += 2
            else:
                sym = s[i]
                num += symDict[sym]
                i+=1
        
        return num