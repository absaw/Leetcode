class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = max(nums)
        currMax, currMin = 1, 1

        for n in nums:
            tmp = n*currMax
            currMax = max(n*currMax, n*currMin, n)
            currMin = min(tmp, n*currMin, n)
            result = max(result,currMax)
        return result