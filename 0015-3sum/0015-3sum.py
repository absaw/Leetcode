class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        result = []
        for i, num in enumerate(nums):

            if i>0 and num==nums[i-1]:
                continue
            
            l = i+1
            r = len(nums)-1

            while l<r:

                tripletSum = num + nums[l] + nums[r]

                if tripletSum > 0:
                    r -=1
                elif tripletSum <0:
                    l += 1
                
                else:
                    result.append([num,nums[l],nums[r]])
                    l+=1
                    r-=1

                    while l<r and nums[l]==nums[l-1]:
                        l += 1
                    while l<r and nums[r]==nums[r+1]:
                        r -= 1
        
        return result
