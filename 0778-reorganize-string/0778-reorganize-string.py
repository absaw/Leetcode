from collections import Counter
import heapq
class Solution:
    def reorganizeString(self, s: str) -> str:
        maxHeap = Counter(s)
	
        maxHeap = [[-ctr,char] for char, ctr in maxHeap.items()]
        heapq.heapify(maxHeap)

        prev = None
        res = ""
        while maxHeap or prev:
            if prev and not maxHeap:
                return ""
            
            ctr,char = heapq.heappop(maxHeap)
        
            ctr += 1
            res += char
            if prev:
                heapq.heappush(maxHeap,prev)
                prev = None
            if ctr !=0:
                prev = [ctr,char]
        
        return res