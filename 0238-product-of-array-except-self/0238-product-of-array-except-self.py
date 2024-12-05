class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        num = [1, 2,  3, 4]
        pre = [1, 1,  2, 6]
       post = [24,12, 4, 1]
        '''

        prefix = [1]*len(nums)

        for i in range(1,len(nums)):
            prefix[i]=prefix[i-1]*nums[i-1]
        postfix = [1]*len(nums)
        for i in range(len(nums)-2,-1,-1):
            postfix[i] = postfix[i+1]*nums[i+1]
        for i in range(len(nums)):
            postfix[i] *= prefix[i]
        
        return postfix