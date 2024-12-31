class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        result = []

        def dfs(i, currSum, curr):
            if currSum == target:
                result.append(curr.copy())
                return
            if currSum > target or i >= len(candidates):
                return
            curr.append(candidates[i])
            dfs(i, currSum+candidates[i],curr)
            curr.pop()
            dfs(i+1, currSum, curr)
        dfs(0,0,[])
        return result
