class Solution:
    def isValid(self, s: str) -> bool:

        if len(s)%2 != 0:
            return False

        p_dict = {
                    '}' : '{',
                    ']' : '[',
                    ')' : '('
                }
        stack = []
        for character in s:
            if character in "({[":
                stack.append(character)
            elif character in ")}]":
                if not stack or p_dict[character] != stack[-1]:
                    return False
                stack.pop()
        return True if not stack else False