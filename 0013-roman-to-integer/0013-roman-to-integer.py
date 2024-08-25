class Solution:
    def romanToInt(self, s: str) -> int:
        
        def get_val(c):
            if c == "I":
                return 1
            elif c == "V":
                return 5
            elif c == "X":
                return 10
            elif c == "L":
                return 50
            elif c == "C":
                return 100
            elif c == "D":
                return 500
            elif c == "M":
                return 1000
        
        i = 0
        num = 0
        n = len(s)
        
        while i < n:

            if i in range(n-1) and get_val(s[i+1]) > get_val(s[i]):
                num += get_val(s[i+1])-get_val(s[i])
                i += 2
            else:
                num += get_val(s[i])
                i += 1
        
        return num

            