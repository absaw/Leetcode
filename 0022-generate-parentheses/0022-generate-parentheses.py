class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        left = 0
        right = 0
        stack = []
        result = []

        def dfs(left, right):
            if left == n and right == n:
                result.append("".join(stack))
                return             
            if left < n:
                stack.append("(")
                dfs(left+1,right)
                stack.pop()

            if right < left:
                stack.append(")")
                dfs(left,right+1)
                stack.pop()
        dfs(0,0)
        return result