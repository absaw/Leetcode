class Solution:
    def isPalindrome(self, s: str) -> bool:

        #convert string to lower case
        # set left pointer at start of string
        # and right pointer at end
        # while l <= r
        # if lef char is not alnum : l+=1 continue
        # if right char is not alnum: r -= 1 continue
        # if not equal, return false
        # inc left ptr; dec right ptr
        # return true at end

        # n,:ay,,,,an
        s = s.lower()

        l = 0
        r = len(s)-1

        while l <= r:
            if not s[l].isalnum():
                l += 1
                continue
            if not s[r].isalnum():
                r -= 1
                continue
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1

        return True


