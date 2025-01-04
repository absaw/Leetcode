class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        import heapq
        intervals.sort()

        res = {}
        i = 0
        minHeap = []
        for q in sorted(queries):
            # adding valid intervals to heap for this query
            while i < len(intervals) and intervals[i][0] <= q:
                l, r = intervals[i]
                size = r-l+1
                heapq.heappush(minHeap, [size, r])
                i += 1
            
            # popping invalid intervals from heap 
            while minHeap and minHeap[0][1]<q:
                heapq.heappop(minHeap)
            # adding top of minHeap to result
            if minHeap:
                size, r = minHeap[0]
                res[q] = size
            else:
                res[q] = -1
        
        return [res[q] for q in queries]

