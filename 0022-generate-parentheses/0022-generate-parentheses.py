class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        result = []
        stack = []
        openN = 0
        closeN = 0
        def backTrack(openN,closeN):

            if openN == n and closeN == n:
                result.append("".join(stack))
                return
            # branch for adding open bracket

            if openN < n:
                stack.append("(")
                backTrack(openN+1,closeN)
                stack.pop()
            
            # branch for adding close bracket

            if closeN < openN:
                stack.append(")")
                backTrack(openN,closeN+1)
                stack.pop()
        backTrack(0,0)
        return result