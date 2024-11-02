class Solution:
    def findMin(self, nums: List[int]) -> int:
        

        l = 0
        r = len(nums)-1
        # 4, 5, 6, 7, 0, 1, 2
        while l < r:
            if nums[l]<=nums[r]:
                return nums[l]
            mid = (l+r)//2

            if nums[l] <= nums[mid]:
                l = mid+1
            elif nums[l]>nums[mid]:
                r = mid
        return nums[l]
