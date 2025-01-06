class TimeMap:

    def __init__(self):
        self.timeDict = collections.defaultdict(list)


    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeDict[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        
        if key not in self.timeDict:
            return ""
        times = self.timeDict[key]
        l = 0
        r = len(times)-1
        ans = -1
        while l<=r:
            mid = l + (r-l)//2

            if times[mid][0] == timestamp:
                ans = mid
                break
            if times[mid][0]< timestamp:
                ans = mid
                l = mid+1
            else:
                r = mid-1
        
        return times[ans][1] if ans != -1 else ""



# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)