class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n
    
        # 1, 2,  3,  4
        # 1  1   2   6
        # 24 12  4   1
        #    12   8  6
        for i in range(1, n):
            result[i] = result[i-1]*nums[i-1]
        
        # calculate postfix
        post = 1
        for i in range(n-2,-1,-1):
            post = post*nums[i+1]
            result[i] = result[i]*post
        
        return result

