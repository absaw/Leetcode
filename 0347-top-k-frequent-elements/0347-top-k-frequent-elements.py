'''
[4,5,6,7,4,1,2,4,1,1,1,2,]

top k = 2
1:4
2: 2
4: 3
5: 1
6: 1
7:1
minheap of length = k

minHeap([freq,num])
if currFreq > minHeap[-1][0]:
    heapq.heappushpop(minHeap,[currFreq,num])
else:
    heapq.heappop()
'''
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = {}

        for num in nums:
            freq[num] = 1 + freq.get(num,0)
        #freq = {number 1: frequency 4, 2: 3, 3:5}
        minHeap = []
        heapq.heapify(minHeap)
        for num,freq in freq.items():
            # if len(minHeap)<k:
            heapq.heappush(minHeap,[freq,num])
            if len(minHeap)>k:
                heapq.heappop(minHeap)
            
        result = []
        i = 0
        while i<k and i < len(minHeap):
            result.append(heapq.heappop(minHeap)[1])
        return result
