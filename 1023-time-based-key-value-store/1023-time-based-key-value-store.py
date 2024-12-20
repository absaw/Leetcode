class TimeMap:

    def __init__(self):
        self.dict = collections.defaultdict(list)
        '''
        {
            foo: [[foo,bar],[1,3]]
        }
        
        '''

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dict:

            self.dict[key].append([value])
            self.dict[key].append([timestamp])
        else:
            self.dict[key][0].append(value)
            self.dict[key][1].append(timestamp)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dict:
            return ""
        vals = self.dict[key][0]
        nums = self.dict[key][1]
        # [ 1,2,4,5,6,7,9,10]

        l = 0
        r = len(nums)-1
        ans = -1
        while l<=r:
            mid = l + (r-l)//2
            if nums[mid] <= timestamp:
                ans = mid
                l = mid+1
            else:
                r = mid-1
        return vals[ans] if ans>-1 else ""



# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)