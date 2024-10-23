class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        # check if the curr substring is a divisor of the total length of the string.
        n = len(s)
        for i in range(1,len(s)//2+1):

            if n % i==0:
                new_s = s[:i] * (n//i)
                if new_s == s:
                    return True
        return False