class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        
        if len(a)>len(b):
            if b in a:
                return 1
        
        #a = list(a)
        #b = list(b)
        
        multiply = len(b)//len(a)
        new_a = a * multiply
        k = 0
        while k<=3:
            if b in new_a:
                return multiply+k
            new_a += a
            k+=1
        return -1