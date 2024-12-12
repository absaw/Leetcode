class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        lm = [0]*n
        rm = [0] * n
        # lm[1]=height[0]
        for i in range(1,n):
            lm[i] = max(lm[i-1],height[i-1])
        for i in range(n-2,-1,-1):
            rm[i] = max(rm[i+1],height[i+1])
        print(lm)
        print(rm)
        #calc water
        water = 0
        for i in range(n):
            if (min(lm[i],rm[i]) - height[i])>0:
                water += min(lm[i],rm[i]) - height[i]
        return water