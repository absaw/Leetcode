class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        if len(nums1)<=len(nums2):
            A = nums1
            B = nums2
        else:
            A = nums2
            B = nums1
        
        l = 0
        r = len(A)-1
        total = (len(A)+len(B))
        half  =total//2
        # A = 1, 4, 6, 7
        #        i
        #     l  
        #        m=1
        #              r

        # B = 2, 4, 5, 8, 10, 11
        #           j
        i = 0
        j = 0
        while True:

            mid = l + (r-l)//2 #1
            i = mid  # 1
            j = half - (mid+1) - 1 # 2
            Aleft = A[i] if i>=0 else float('-inf')
            Aright = A[i+1] if (i+1) < len(A) else float('inf')
            Bleft = B[j] if j >=0 else float('-inf')
            Bright = B[j+1] if (j+1)<len(B) else float('inf')
            
            if Aleft<=Bright and Bleft <= Aright:
                if total%2 == 0:
                    return (max(Aleft,Bleft)+min(Aright,Bright))/2
                return min(Aright,Bright)
            
            elif Aleft>Bright:
                r = mid-1
            else:
            # elif Bleft>Aright:
                l = mid+1
            



            
