'''
og arr  new arr(having max at each point)
1       1
2       2 = max(ignoring 2(=1), considering 2(=2)) 
3       4 = max(ignoring 3(taking prev val = 2), considering 3(= 3+arr[i-2]))
1       4 = max(ignoring 1(=4), considering 1(=1+arr[i-2]=1+2=3))
'''

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<=2:
            return max(nums)
        maxArr = [0]*len(nums)
        maxArr[0] = nums[0]
        maxArr[1] = max(nums[1],nums[0])
        for i in range(2,len(nums)):
            maxArr[i] = max(maxArr[i-1], nums[i]+maxArr[i-2])
        return maxArr[-1]