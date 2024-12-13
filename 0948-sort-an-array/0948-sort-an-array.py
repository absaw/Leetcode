class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        # merge sort
        def merge(a,l,m, r):
            L = a[l:m+1]
            R = a[m+1:r+1]
            i = j = 0
            k = l

            while i < len(L) and j < len(R):
                if L[i] < R[j]:
                    a[k] = L[i]
                    i+=1
                else:
                    a[k] = R[j]
                    j += 1
                k += 1
            while i < len(L):
                a[k] = L[i]
                i += 1
                k += 1
            while j < len(R):
                a[k] = R[j]
                k += 1
                j += 1

        def merge_sort(a, l, r):

            if l==r:
                return
            mid = (l+r)//2
            merge_sort(a,l,mid)
            merge_sort(a,mid+1,r)
            merge(a,l,mid,r)
        
        merge_sort(nums,0,len(nums)-1)

        return nums