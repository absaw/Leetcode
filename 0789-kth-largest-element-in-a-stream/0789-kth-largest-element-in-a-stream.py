import heapq
class KthLargest:

        def __init__(self, k, nums):
            self.minHeap = nums
            self.k = k
            heapq.heapify(self.minHeap)
            while len(self.minHeap)>self.k:
                heapq.heappop(self.minHeap)

        def add(self, val:int)-> int:
            if len(self.minHeap)==self.k and  val > self.minHeap[0]:
                heapq.heappush(self.minHeap,val)
                heapq.heappop(self.minHeap)
            elif len(self.minHeap)<self.k:
                heapq.heappush(self.minHeap,val)
            return self.minHeap[0]
            


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)