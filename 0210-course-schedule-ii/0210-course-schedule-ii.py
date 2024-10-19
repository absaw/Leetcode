class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        courseMap = {}

        for crs in range(numCourses):
            courseMap[crs]=[]
        
        for crs, pre in prerequisites:
            courseMap[crs].append(pre)

        output=[]
        visited, current_run = set(), set()
        def dfs(crs):

            if crs in current_run:
                return False
            if crs in visited:
                return True
            
            current_run.add(crs)
            for pre in courseMap[crs]:
                if not dfs(pre):
                    return []
            current_run.remove(crs)
            visited.add(crs)
            output.append(crs)
            courseMap[crs] = []

            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return []
        
        return output



