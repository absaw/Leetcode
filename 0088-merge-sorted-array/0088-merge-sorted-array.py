class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        n1 = nums1.copy()

        p1 = p2 = k = 0

        while p1 < m and p2 < n:

            if n1[p1] < nums2[p2]:
                nums1[k] = n1[p1]
                p1 += 1
            else:
                nums1[k] = nums2[p2]
                p2 += 1
            
            k += 1
        
        while p1 < m:
            nums1[k] = n1[p1]
            p1 += 1
            k += 1
        while p2 < n:
            nums1[k] = nums2[p2]
            p2 += 1
            k += 1
        
        