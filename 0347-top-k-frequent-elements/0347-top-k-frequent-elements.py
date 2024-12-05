class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import heapq

        freqD = {}

        for n in nums:
            freqD[n] = 1 + freqD.get(n,0)
        heap = []
        heapq.heapify(heap)
        for n, freq in freqD.items():
            heapq.heappush(heap,[freq,n])
            if len(heap)>k:
                heapq.heappop(heap)
        result = []
        for i in range(k):
            if heap:
                result.append(heapq.heappop(heap)[1])
        return result