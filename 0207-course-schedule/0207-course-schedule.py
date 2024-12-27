class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list ={}

        for course in range(numCourses):
            adj_list[course] = []
        # [1,0],[2,3],[3,1]
        # 0: []
        # 1: [0]
        # 2: [3]
        # 3: [1]
        # 2 > 3 > 1 > 0
        for a, b in prerequisites:
            adj_list[a].append(b)
        
        #i have to detect if there exists a loop in the graph
        # if there is a loop, then the dependency can't be fulfilled
        # for each of the nodes, if there are no neighbors, it can be taken. so no loop
        # for node with neighbor, all the neighbors must be traversed without any loop
        visited = set()
        rec_stack = set()
        def dfs(course):
            if course in rec_stack:
                return False
            # if not adj_list[course]:
            #     return True
            if course in visited:
                return True
            visited.add(course)
            rec_stack.add(course)
            can_complete = True
            for neighbor in adj_list[course]:
                can_complete = can_complete and dfs(neighbor)
            rec_stack.remove(course)
            return can_complete
            
        self.result = True

        for course in range(numCourses):
            # if course not in visited:
            self.result = self.result and dfs(course)
        return self.result                
