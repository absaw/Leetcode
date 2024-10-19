# from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courseMap = {}
        for course in range(numCourses):
            courseMap[course] = []
        for course,pre in prerequisites:
            courseMap[course].append(pre)
        
        visited = set()

        def dfs(course):

            if course in visited:
                # print('false1',course)
                return False
            
            if courseMap[course] == []:
                return True
        
            visited.add(course)

            for pre in courseMap[course]:

                if not dfs(pre): 
                    # print('false2',course)

                    return False
            
            visited.remove(course)
            courseMap[course] =[]
            return True
        
        for course in range(numCourses):
            if not dfs(course): 
                # print('false3',course)
                
                return False
        
        return True
        