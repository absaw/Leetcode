class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        

        res = []
        
        def backTrack(i,sol,total):
            
            if total == target:
                res.append(sol.copy())
                return
            
            if total > target or i == len(candidates):
                return
            
            #Exclude the current element
            backTrack(i+1,sol,total)

            #include the current element
            sol.append(candidates[i])
            backTrack(i,sol,total+candidates[i])
            sol.pop()
            
        
        backTrack(0,[],0)

        return res