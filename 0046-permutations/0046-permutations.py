class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        if len(nums) == 0:
            return [[]]
        result = []
        permutations = self.permute(nums[1:])
        val = nums[0]
        # print(val)
        # print(permutations)
        for perm in permutations:
            # print(perm)
            for i in range(len(perm)+1):
                
                perm_copy = perm.copy()
                perm_copy.insert(i,val)
                # print(perm_copy)
                result.append(perm_copy)
        # print(result)
        return result
