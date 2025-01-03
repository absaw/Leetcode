'''
maxHeap to store the stones.
while len(maxHeap)>1:
    y = maxHeap.pop
    x = maxHeap.pop
    if y!=x:
        maxHeap.push(y-x)
return maxHeap[0]
'''
import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        maxHeap = [-stone for stone in stones]
        heapq.heapify(maxHeap)
        while len(maxHeap)>1:
            y = -heapq.heappop(maxHeap)
            x = -heapq.heappop(maxHeap)
            if y!=x:
                heapq.heappush(maxHeap,-(y-x))
        return -maxHeap[0] if maxHeap else 0