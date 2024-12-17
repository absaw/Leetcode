class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        result = 0
        for s in tokens:

            if s in "*/+-":
                #operator
                op1 = int(stack.pop())
                op2 = int(stack.pop())
                operation = 0
                if s == "+":
                    operation = op1 + op2
                elif s == "-":
                    operation = op2 - op1
                elif s == "*":
                    operation = op1 * op2
                else:
                    operation = int(op2/op1)
                stack.append(operation)
            else:
                #number: just append
                n = int(s)
                stack.append(n)
        return stack[0]