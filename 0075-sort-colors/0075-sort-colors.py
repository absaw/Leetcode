
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        bucket = [0,0,0]
    
        for n in nums:
            bucket[n] += 1

        nums[:bucket[0]] = [0]*bucket[0]
        nums[bucket[0]:bucket[0]+bucket[1]] = [1] * bucket[1]
        nums[bucket[0]+bucket[1]:bucket[0]+bucket[1]+bucket[2]]=[2] * bucket[2]
        print(nums)
        return nums