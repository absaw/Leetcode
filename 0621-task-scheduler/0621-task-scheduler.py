import heapq
'''
Using  heap to maintain the most frequent task at top
once that is popped, it is added to queue with the next point of time from when it can be used. 
if this time is reached, then the count is added back to the heap
'''
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        freqTask = Counter(tasks)
        maxHeap = [-freq for freq in freqTask.values()] # freq

        heapq.heapify(maxHeap)

        queue = collections.deque()
        time = 0
        while maxHeap or queue:
            time += 1
            if maxHeap:
                top_count = -heapq.heappop(maxHeap)-1

                if top_count>0:
                    queue.append([top_count, time+n])
            
            if queue and queue[0][1]==time:
                heapq.heappush(maxHeap,-queue.popleft()[0])
            
        return time


        