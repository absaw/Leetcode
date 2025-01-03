'''
calc distances of all points
minHeap to store [distance, (x,y)]
pop till we have k points
'''
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        def getDistance(x,y):
            return math.sqrt(x**2+y**2)
        
        minHeap = []

        for x, y in points:
            heapq.heappush(minHeap, [getDistance(x,y), [x,y]])
        res = []
        while len(res)<k:
            res.append(heapq.heappop(minHeap)[1])

        return res