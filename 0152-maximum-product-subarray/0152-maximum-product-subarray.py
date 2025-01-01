'''
Since negative values can be present, each new number can flip the 
max product. so a good way would be to keep a min and max number 
which can help us choose which of them should the current number
be multiplied with to maintain the max of possible values
        [2, 3, -2, 4]  -1
currMax  2  6  6   24    48
currMin  2  2  -12 -48  -48
res      2  6  6   24    48
'''
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        result = max(nums)

        curMax = 1
        curMin = 1

        for n in nums:
            tmp = curMax*n
            curMax = max(curMax*n, curMin*n, n)
            curMin = min(tmp, curMin*n, n)
            result = max(curMax,result)

        return result