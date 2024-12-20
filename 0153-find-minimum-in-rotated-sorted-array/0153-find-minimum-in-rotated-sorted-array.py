class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        l = 0
        r = len(nums) - 1
        ans = nums[0]
        while l <= r:
            if nums[l]<=nums[r]:
                ans = min(ans,nums[l])
                break
            mid = l + (r-l)//2
            ans = min(ans,nums[mid])
            if nums[mid] >= nums[l]:
                l = mid+1
            elif nums[mid] < nums[l]:
                r = mid-1

        return ans