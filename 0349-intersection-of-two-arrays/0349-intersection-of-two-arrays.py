class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        interSet = set(nums1)
        intersection = []
        for num in nums2:
            if num in interSet:
                intersection.append(num)
                interSet.remove(num)
        return intersection
