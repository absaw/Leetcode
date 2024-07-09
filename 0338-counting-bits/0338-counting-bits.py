class Solution:
    def countBits(self, n: int) -> List[int]:
        
        offset = 1
        count = [0] * (n+1)

        for i in range(1,n+1):

            if i == offset*2:
                offset = i
            
            count[i] = 1 + count[i - offset]
        return count