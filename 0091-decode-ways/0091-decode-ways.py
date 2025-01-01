'''
1 1 1 0 6
1,1,
1,11

1, 1
1, 1, 1,
1, 1, 1, 0 x
1, 1, 1, 06 x
1, 1, 10, 6
sol = s[i] + s[] 
min: 1:A
max: 26: Z, 2 characters
at each point i have the options
take 1 character provided its not zero
take 2 characters, provided it is between 1 and 26
if the current branch reaches the end with all valid characters, then increase valid count
'''

class Solution:
    def numDecodings(self, s: str) -> int:
        
        memo = {len(s):1}
        # s="226"
        #    ^
        # ways = 0
        def dfs(i):

            if i in memo:
                return memo[i]
            if i > len(s) or s[i]=="0":
                return 0
            
            ways = dfs(i+1)
            if (i<len(s)-1 and 
                (s[i]=="1" or s[i]=="2" and s[i+1]<'7')):
                ways += dfs(i+2)
            
            memo[i] = ways
            return memo[i]
        
        dfs(0)
        # print(memo)
        return memo[0] if 0 in memo else 0



