class Solution:
    def trap(self, height: List[int]) -> int:
        # O(1)

        leftMax=0
        rightMax = 0

        l = 0
        r = len(height)-1
        water = 0
        while l<=r:

            if leftMax <= rightMax:

                if height[l]>leftMax:
                    leftMax = height[l]
                else:
                    water += leftMax-height[l]
                l += 1
            else:

                if height[r] > rightMax:
                    rightMax = height[r]
                else:
                    water += rightMax - height[r]
                r -= 1
        return water