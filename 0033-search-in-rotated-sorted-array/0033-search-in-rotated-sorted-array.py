'''
4, 5, 6, 7, 0, 1, 2
l
                  r
         m

target = 5

while l<=r:

    calc mid
    if nums[mid]>nums[l]:
        if target < nums[mid]:
            move right
        else:
            move left
    elif nums[mid]<nums[l]:
        if target>nums[mid]:
            move right
        else: 
            move left

'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        ans = -1
        while l <= r:
# 4, 5, 6, 7, 0, 1, 2
# l
#                   r
#           m
            mid = l + (r-l)//2
            if nums[mid] == target:
                ans = mid
                break
            if nums[mid] >= nums[l]:
                # large sorted section
                if target in range(nums[l],nums[mid]+1):
                    r = mid-1
                else:
                    l = mid+1
            else:
                #small sorted section
                if target in range(nums[mid],nums[r]+1):
                    l = mid+1
                else:
                    r = mid-1
        return ans


