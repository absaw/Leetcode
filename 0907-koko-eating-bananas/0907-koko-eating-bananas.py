'''
piles = [3, 6, 7, 11]
h = 8
k = bananas per hour such that it is the min no. of bananas needed
to finish within 8 hrs
max k = 11 bananas, so 4 hours are enough to complete all the piles
min k ?
count_hours(k):
    loop over piles,
    reduce each element by k utill all elements are zero
    i.e. h = 
'''
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l = 1
        r = max(piles)
        res = r
        def get_hours(k):
            h = 0
            for p in piles:
                h += math.ceil(p/k)
            return h
        
        while l<=r:
            mid = (l+r)//2

            hours = get_hours(mid)

            #if hours are more than asked, eat faster
            if hours>h:
                l = mid+1
            # if hours are less than asked, we can eat at this rate but also slower. so update the result and eat slower, 
            else:
                r = mid-1
                res = min(res,mid)
            
        return res