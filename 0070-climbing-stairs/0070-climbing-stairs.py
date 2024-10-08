class Solution:
    def climbStairs(self, n: int) -> int:
        
        one = two = 1
        # 1, 1, 2, 3, 5, 8
        for i in range(n-1):
            temp = two
            two = one + two
            one = temp
        return two