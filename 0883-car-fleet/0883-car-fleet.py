'''
position= [10,8,0,5,3]
diff    = [2,4,12,7,9]
speed =   [2,4,1,1,3]
target = 12

p = 12,12,1,6,6
p = 12,12,2,7,7
p = 12,12,3,8,8
'''
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        psPair = []
        for i in range(len(position)):
            psPair.append([position[i],speed[i]])
        psPair.sort(key = lambda x: x[0],reverse=True)
        stack = []
        for pos, speed in psPair:
            stack.append((target-pos)/speed)
            if len(stack)>=2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)