class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sCounter = collections.Counter(s)
        tCounter = collections.Counter(t)
        return sCounter==tCounter