class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_mat = {course:[] for course in range(numCourses)}

        for a,b in prerequisites:
            adj_mat[a].append(b)
        self.order_stack = []
        self.visited = set()
        self.visit_branch =set()
        def dfs(course):
            if course in self.visit_branch:
                return False
            if course in self.visited:
                return True
            
            self.visit_branch.add(course)
            #neighbors
            for neighbor in adj_mat[course]:
                if neighbor not in self.visited:
                    if not dfs(neighbor):
                        return False
            self.visit_branch.remove(course)
            self.visited.add(course)
            self.order_stack.append(course)
            return True

        for course in adj_mat:
            if course not in self.visited:
                if not dfs(course):
                    return []
        return self.order_stack
