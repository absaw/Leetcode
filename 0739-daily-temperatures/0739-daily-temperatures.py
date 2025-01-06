class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = [] # append (val,index)
        result = [0]*len(temperatures)
        for i,temp in enumerate(temperatures):
            if not stack:
                stack.append((i,temp))
                continue
            
            while stack and stack[-1][1] < temp:
                i_top, t_top = stack.pop()
                result[i_top] = i - i_top
            
            stack.append((i,temp))
        
        return result






