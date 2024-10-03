class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        n = len(nums)
        total_sum = sum(nums)
        target = total_sum % p
        
        if target == 0:
            return 0
        
        prefix_sum = 0
        seen = {0: -1}
        min_length = n
        
        for i, num in enumerate(nums):
            prefix_sum = (prefix_sum + num) % p
            complement = (prefix_sum - target) % p
            
            if complement in seen:
                min_length = min(min_length, i - seen[complement])
            
            seen[prefix_sum] = i
        
        return min_length if min_length < n else -1