class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        p1 = 0
        p2 = 0
        mergedNums = [0]*(len(nums1)+len(nums2))
        k = 0
        median = 0.0
        while k < len(mergedNums):
            # p1 = None if p1==len(nums1) else p1
            # p2 = None if p2==len(nums2) else p2
            # print(p1,p2)
            if p1<len(nums1) and p2<len(nums2):
                if nums1[p1] < nums2[p2]:
                    mergedNums[k] = nums1[p1]
                    p1 += 1
                else:
                    mergedNums[k] = nums2[p2]
                    p2 += 1
            elif p1<len(nums1):

                mergedNums[k] = nums1[p1]
                p1+=1
            elif p2<len(nums2):
                mergedNums[k] = nums2[p2]
                p2+=1
            k+=1
        mergedLen = len(mergedNums)
        # print(mergedNums)
        if mergedLen % 2 == 0:
            m1 = mergedLen//2
            m2 = m1 -1
            median = (mergedNums[m1]+mergedNums[m2])/2
        else:
            m1 = mergedLen//2
            median = mergedNums[m1]

        return median


