import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap = nums
        self.capacity = k
        heapq.heapify(self.minHeap)
        while len(self.minHeap)>self.capacity:
            heapq.heappop(self.minHeap)
        
    def add(self, val: int) -> int:
        
        if len(self.minHeap)==self.capacity and val>self.minHeap[0]:
            heapq.heappushpop(self.minHeap,val)
        elif len(self.minHeap)<self.capacity:
            heapq.heappush(self.minHeap,val)

        return self.minHeap[0]



# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)