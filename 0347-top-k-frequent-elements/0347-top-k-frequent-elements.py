import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        minHeap = []
        countDict = {}

        for number in nums:
            countDict[number] = 1 + countDict.get(number,0)

        for num, freq in countDict.items():
            heapq.heappush(minHeap,(freq,num))
            
            if len(minHeap)>k:
                heapq.heappop(minHeap)

        result = []
        for i in range(len(minHeap)):
            result.append(heapq.heappop(minHeap)[1])
        return result