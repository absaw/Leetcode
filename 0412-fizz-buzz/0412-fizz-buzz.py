class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = []
        for i in range(1,n+1):
            res = ""
            if i %3==0 and i % 5 == 0:
                res = "FizzBuzz"
            elif i % 3==0:
                res = "Fizz"
            elif i % 5 == 0:
                res = "Buzz"
            else:
                res = str(i)
            result.append(res)
        return result