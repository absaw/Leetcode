class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        countArr = [[] for i in range(len(nums)+1)]

        freqD = {}

        for n in nums:
            freqD[n] = 1 + freqD.get(n,0)
        
        for num, freq in freqD.items():
            countArr[freq].append(num)
        result = []
        for i in range(len(nums),0,-1):
            for num in countArr[i]:
                if len(result)<k:
                    result.append(num)
                else:
                    return result
        return result
        