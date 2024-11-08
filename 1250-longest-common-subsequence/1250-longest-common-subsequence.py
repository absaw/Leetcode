class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        memo = {} #(ch1,ch2)

        def findMax(ptr1, ptr2):
            
            if ptr1 == len(text1) or ptr2 == len(text2):
                return 0
            
            if (ptr1,ptr2) in memo:
                return memo[(ptr1,ptr2)]
            else:
                if text1[ptr1] == text2[ptr2]:
                    memo[(ptr1,ptr2)] = 1 + findMax(ptr1+1,ptr2+1)
                else:
                    memo[(ptr1,ptr2)] = max(findMax(ptr1+1,ptr2),findMax(ptr1,ptr2+1))
            
            return memo[(ptr1,ptr2)]

        findMax(0,0)
        return memo[(0,0)]


