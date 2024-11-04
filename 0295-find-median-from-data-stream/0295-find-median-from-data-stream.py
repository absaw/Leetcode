import heapq
class MedianFinder:

    def __init__(self):
        self.smallHeap = [] #maxHeap
        self.bigHeap = [] #minHeap
        heapq.heapify(self.smallHeap)
        heapq.heapify(self.bigHeap)

    def addNum(self, num):
        heapq.heappush(self.smallHeap,-num)
        if self.bigHeap and (-self.smallHeap[0] > self.bigHeap[0]):
            heapq.heappush(self.bigHeap,-heapq.heappop(self.smallHeap))
        if abs(len(self.smallHeap)-len(self.bigHeap))>1:
            if len(self.smallHeap)>len(self.bigHeap):
                heapq.heappush(self.bigHeap,-heapq.heappop(self.smallHeap)) 
            else:
                heapq.heappush(self.smallHeap,-heapq.heappop(self.bigHeap)) 
            
    def findMedian(self)->float:
        # if (len(self.bigHeap)+len(self.smallHeap) %2 !=0:
        # print(self.smallHeap)
        # print(self.bigHeap)
        if len(self.bigHeap)>len(self.smallHeap):
            return self.bigHeap[0]
        elif len(self.bigHeap)<len(self.smallHeap):
            return -self.smallHeap[0]
        else:
            return (self.bigHeap[0]-self.smallHeap[0])/2

        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()