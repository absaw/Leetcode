class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        greatDict = {}

        stack = []

        for num in nums2:

            while stack and num > stack[-1]:
                topElement = stack.pop()
                greatDict[topElement]=num
            stack.append(num)
        ans = [-1] * len(nums1)
        for i,num in enumerate(nums1):
            if num in greatDict:
                ans[i] = greatDict[num]
        return ans
        