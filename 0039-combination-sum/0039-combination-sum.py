class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.res = []

        def combinations(nums,currPtr,currSum):

            if currSum == target:
                self.res.append(nums[:])
                return
            elif currSum > target or currPtr == len(candidates):
                return
            
            #using the current element
            currSum += candidates[currPtr]
            nums.append(candidates[currPtr])

            combinations(nums,currPtr,currSum)
            #avoiding the current element
            currSum -= candidates[currPtr]
            nums.pop()
            combinations(nums,currPtr+1,currSum)
        combinations([],0,0)
        return self.res
            