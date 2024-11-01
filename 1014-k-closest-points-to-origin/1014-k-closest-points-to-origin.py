import heapq, math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []
        heapq.heapify(maxHeap)
        for x,y in points:
            distance = math.sqrt(x**2+y**2)
            # maxHeap.append([-distance,(x,y)])
            heapq.heappush(maxHeap,[-distance,(x,y)])

            

        # heapq.heapify(maxHeap)
        res = []
        while len(maxHeap)!=0:
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)
            else:
                res.append(heapq.heappop(maxHeap)[1])
        return res
