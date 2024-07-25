class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        # [1,2,3]

        res, sol = [], []
        n = len(nums)
        def backTrack(i):
            pass
            if i == n:
                res.append(sol.copy())
                return
            backTrack(i+1)

            sol.append(nums[i])
            backTrack(i+1)
            sol.pop()
            
        backTrack(0)

        return res
        