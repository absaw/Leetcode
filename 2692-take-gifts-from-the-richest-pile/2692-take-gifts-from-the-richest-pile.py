class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        import heapq
        maxHeap = [-gift for gift in gifts]
        heapq.heapify(maxHeap)

        while k!=0:
            k -= 1
            maxElement = -heapq.heappop(maxHeap)
            heapq.heappush(maxHeap, -math.floor(math.sqrt(maxElement)))
        
        return -sum(maxHeap)

