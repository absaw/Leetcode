class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums)%k != 0:
            return False
        nums.sort(reverse=True)
        n = len(nums)
        used = [False] * n
        target = sum(nums)//k
        # nums = [4,3,2,3,5,2,1], k = 4
        #         i
        def backTrack(i,k, currSum):
            if k == 0:
                return True
            
            if currSum == target:
                return backTrack(0, k-1, 0)
            
            for j in range(i, n):
                if used[j] or currSum + nums[j] > target:
                    continue
                used[j] = True
                if backTrack(j+1, k, currSum+nums[j]):
                    return True
                
                used[j] = False
                if currSum == 0:
                    return False
            return False
        
        return backTrack(0, k, 0)
        