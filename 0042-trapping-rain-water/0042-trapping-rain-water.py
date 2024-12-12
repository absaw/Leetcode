class Solution:
    def trap(self, height: List[int]) -> int:
        
        l = 0
        r = len(height)-1
        lm = height[l]
        rm = height[r]
        water = 0
        while l<=r:
            if lm<=rm:
                if height[l]<lm:
                    water += lm - height[l]
                else:
                    lm = height[l]
                l+= 1
            else:
                if height[r]<rm:
                    water += rm - height[r]
                else:
                    rm = height[r]
                r -= 1
            
        return water
        