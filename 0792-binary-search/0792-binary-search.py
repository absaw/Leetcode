class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def searchNums(nums, l, r):
            if l>r:
                return -1
            mid = (l+r) // 2
            
            if nums[mid] == target:
                return mid
            
            elif nums[mid] < target:
                return searchNums(nums,mid+1,r)
            
            elif nums[mid] > target:
                return searchNums(nums,l,mid-1)
        
        return searchNums(nums,0,len(nums)-1)