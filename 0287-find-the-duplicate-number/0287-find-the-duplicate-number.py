'''
1,3,4,2,2
  ^
'''
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        # floyd warshall
        # find intersection between fast and slow pointers
        #traverse from start and intersection point, to find second intersection, which is the 
        # final answer

        slow = fast= nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        intersection1 = slow

        ptr=nums[0]

        while ptr!=intersection1:
            ptr = nums[ptr]
            intersection1 = nums[intersection1]
        
        return ptr