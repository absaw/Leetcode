class Solution:
    def maxArea(self, height: List[int]) -> int:
        

        l = 0
        r = len(height)-1
        max_area = 0
        while l <= r:

            area = (r-l) * (min(height[l],height[r]))
            max_area = max(area,max_area)

            if height[l]<height[r]:
                l += 1
            elif height[l]>height[r]:
                r -= 1
            else:
                if (0<= l < r < len(height)) and height[l+1]> height[r-1]:
                    l+=1
                else:
                    r -= 1
            
        return max_area
