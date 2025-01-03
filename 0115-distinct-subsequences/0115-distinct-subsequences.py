class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        '''
        s = rabbbit
            i
        t = rabbit
            j

        at each point if the characters are equal, 
        whether we take a char or not depends if we are incrementing j or not. if inc, 
        then taking that char. and we need to find whole of t in s, so we don't keep i same and inc 
        j, since that would mean skipping a char of t.
        either take the char in s and in t (i+1, j+1)
        or skip the char in s and then check further (i+1,j)
        dp state: (i,j)
        base case: if j == len(t): return 1


        '''
        memo = {}
        if t=="":
            return 1
        elif s == "":
            return 0
        def dfs(i,j):

            if j == len(t):
                return 1
            if i >= len(s):
                return 0
            if (i,j) in memo:
                return memo[(i,j)]
            ways = 0
            if s[i] == t[j]:
                # taking curr char, skipping curr char
                ways = dfs(i+1,j+1) 
            # else:
            ways += dfs(i+1,j)
            memo[(i,j)] = ways
            return ways
        return dfs(0,0)
