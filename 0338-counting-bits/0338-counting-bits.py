'''
   8421
0   000 - 0
1   001 - 1
2   010 - 1  offset = 2
3   011 - 2  offset = 2
4   100 - 1 + (val of last 2 digits=2^0 and 2^1) = 1 + 0
5   101 - 1 +1
6   110 - 1+1
7   111 - 1+ 2
8  1000 - 1 + (val of last 3 digits=2^0 and 2^2)
9  1001 - 1 + (current val - 8 )
10 1010
..
16
  10000 - offset of 16
so the offset starts from 1 and multiplies by 2 every time a power of 2 increases
arr[0 to n+1]
arr[0] = 0
arr[1] = 1
offset = 1
loop from 2 to n+1
    if i %2 == 0:
        offset *= 2
    arr[i] = 1+arr[i-offset]
'''


class Solution:
    def countBits(self, n: int) -> List[int]:
        
        offset = 1
        arr = [0]* (n+1)
        if n>=1:
            arr[0]=0
            arr[1]=1
        for i in range(2,n+1):
            if i == offset<<1:
                offset = offset<<1
            # print(offset)
            # print(arr)
            arr[i] = 1+arr[i-offset]
        return arr