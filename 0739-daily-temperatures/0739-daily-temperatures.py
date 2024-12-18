class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        # question of monotonic DECREASING stack, since the stack only holds
        # values in decreasing order 

        stack = []
        answer = [0]* len(temperatures)

        for i, temp in enumerate(temperatures):

            while stack and stack[-1][0]<temp:
                topElement, topIndex = stack.pop()
                answer[topIndex] = i - topIndex

            stack.append([temp,i])
        return answer

                
