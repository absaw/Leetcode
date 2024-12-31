class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<2:
            return nums[0]
        def helper(nums):
            rob1 = 0
            rob2 = 0
            # rob1, rob2, i, i+1 
            for i in range(len(nums)):
                op1 = nums[i]+rob1
                op2 = rob2
                nums[i] = max(op1,op2)
                # res = max(res,nums[i])
                rob1 = rob2
                rob2 = nums[i]
            return nums[-1]
        return max(helper(nums[:-1]), helper(nums[1:]))