class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        l = 0
        r = 0
        result = []
        queue = collections.deque()
        while r < len(nums):
            #check wether there are any items lesser than current element at right end of q
            while queue and nums[queue[-1]] < nums[r]:
                queue.pop()
            queue.append(r)

            #if left end element is out of sliding window 
            if queue[0] < l:
                queue.popleft()
            
            if r >= (k-1):
                result.append(nums[queue[0]])
                l += 1
            r += 1
        return result


