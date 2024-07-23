class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        def calc(x,n):
            if n == 0:
                return 1
            if x == 0:
                return 0
            res = calc(x,n//2)
            res *= res
            return res if n%2 == 0 else res * x

        result = calc(x,abs(n))

        return result if n>=0 else (1/result)