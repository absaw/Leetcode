'''
n = 2
op = 2
1,1
2
n = 3
1,1,1
1,2
2,1
n=4
1,1,1,1
1,2,1
2,2
2,1,1
1,1,2
base case = 
n=1, ans = 1
n = 2, ans = 1
n = 3, ans = func(n-1)+func(n-2)= func(2)+func(1)
n = 4, ans = func(n-1)+func(n-2) = func(3)+func(2) = func(2)+func(1)+func(2) =  3
'''

class Solution:
    def climbStairs(self, n: int) -> int:
        #base case = n==1, n==2
        if n<=2:
            return n
        memo = [0]*(n+1)
        memo[1] = 1
        memo[2] = 2
        def climb(n):
            # if n==1 or n==2:
            #     return 1
            if memo[n]==0:
                memo[n] = climb(n-1)+climb(n-2)
            return memo[n]
        
        return climb(n)
        