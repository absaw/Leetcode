class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        idx_dict = {}

        for i in range(len(nums)):
            
            if target-nums[i] in idx_dict:
                return [i,idx_dict[target-nums[i]]]
            
            idx_dict[nums[i]] = i
            