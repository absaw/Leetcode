'''
loop through intervals

a    b
   x    y

     a     b
   x    y

ab x    y
   
   x    y a b

before: insert it at that index, return result
after: insert it at end
intersection: 
'''
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        a , b = newInterval
        result = []
        for i in range(len(intervals)):

            x, y = intervals[i]

            if b < x :
                result.append([a,b])
                result+= intervals[i:]
                return result
            elif (x<=a <=y or x<=b<=y):
                a = min(a,x)
                b = max(b,y)
            elif (a>x):
                result.append([x,y])
            
        result.append([a,b])

        return result