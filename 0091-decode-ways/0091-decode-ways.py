'''
12
1, 12
AB, L
o/p = 2

226
2,2,6
2,26
22,6
o/p = 3

06

o/p = 0

11106
subproblems: at each point, I can take 1 digit(if not 0) or 2 digits(if 1st not 0)

1,1106
 ,1,106     11,06 X
    10,6     1,06 X

11,106
  ,10, 6

1.have a dictionary for storing the number of ways for a particular pattern
recursively divide current string into further parts, such that at each point, I can take 1 digit(if not 0) or 2 digits(if 1st not 0)
If the current pattern matches prexisting one, just add it 

'''


class Solution:
    def numDecodings(self, s: str) -> int:
        
        decodeDict = {len(s):1}
        # 11106
        def divide(idx):

            if idx in decodeDict:
                return decodeDict[idx]
            if s[idx]=="0":
                return 0

            res = divide(idx+1)

            if idx+1<len(s) and (s[idx]=="1" or s[idx] == "2" and s[idx+1] in "0123456"):
                res += divide(idx+2)
            
            decodeDict[idx] = res
            return res
        return divide(0)
            

            
