class Solution:
    def reverseBits(self, n: int) -> int:
        
        i = 0

        res = 0

        while i < 32:
            rb = 0
            if ((n & (1<<i)) != 0):
                rb = 1 
            # else:
            #     rb = 0
            mask = rb << (31-i)
            res = mask | res
            i += 1
        
        return res