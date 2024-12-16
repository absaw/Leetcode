'''
k = 3
nums = [1,3,-1,-3,5,3,6,7], 
          l
                r
maxHeap = [3,-1,-3]
result = [3,3]
loop through the nums array
when you go to the next window,
pop the left pointer element from the window
push the righ pointer element into the heap
append top of heap to result
'''
import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        result = []
        maxHeap = []
        heapq.heapify(maxHeap)
        r = k
        
        l = 0
        for i in range(len(nums)):
            if i < k:
                heapq.heappush(maxHeap,(-nums[i],i))
                if i == k-1:
                    result.append(-maxHeap[0][0])
            else:
                r = i
                l += 1
                heapq.heappush(maxHeap,(-nums[i],i))
                while maxHeap[0][1] not in range(l,r+1):
                    heapq.heappop(maxHeap)
                result.append(-maxHeap[0][0])
        return result
