class Solution:
    # O(nlogk solution)
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []
        
        for x, y in points:
            distance = -(x**2 + y**2)  # Use negative to simulate max-heap behavior
            heapq.heappush(maxHeap, (distance, [x, y]))
            
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)  # Remove the farthest point
        
        return [point for _, point in maxHeap]