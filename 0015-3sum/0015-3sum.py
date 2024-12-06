class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()

        result = []

        for i, num in enumerate(nums):

            if num >0:
                break
            if i>0 and nums[i-1] == nums[i]:
                continue
            
            l = i + 1
            r = len(nums)-1

            while l < r:

                threeSum = num + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    result.append([num,nums[l],nums[r]])
                    l += 1
                    r -= 1
                    while nums[l]==nums[l-1] and l < r:
                        l += 1
        return result