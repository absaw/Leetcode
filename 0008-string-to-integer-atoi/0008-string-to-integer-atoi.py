class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s:
            return 0
        
        negative = False
        if s[0] == '-':
            negative = True
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]

        if len(s)==0:
            return 0

        num = 0
        for i in range(len(s)):
            
            ord_s = ord(s[i])
            if ord_s in range(48,58):
                n = ord_s-48
                num = num*10 + n
            else: 
                break
            # if (ord_s in range(48,58)):
            #     num_idx_end += 1
            # else:
            #     break
    
        if negative:
            num = -(num)
   
        if num > (2**31-1):
            num = (2**31)-1
        elif num < (-2**31):
            num = -(2**31)
    
        return num