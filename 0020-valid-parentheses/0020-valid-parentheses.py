class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []

        bracketDict = {
            ')':'(',
            ']':'[',
            '}':'{'
        }

        
        for i in range(len(s)):

            ch = s[i]

            if ch not in bracketDict:
                stack.append(ch)
            else:
                
                # el = stack.pop()
                if not stack or bracketDict[ch] != stack.pop():
                    return False
        
        return True if not stack else False