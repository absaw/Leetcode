import collections 
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        m = len(rooms)
        n = len(rooms[0])
        q = collections.deque()
        visited = set()

        def add_to_q(n_r,n_c):
            if ( n_r not in range(m) or
                 n_c not in range(n) or 
                 (n_r,n_c) in visited or 
                 rooms[n_r][n_c] == -1):
                 return
            q.append((n_r,n_c))
            visited.add((n_r,n_c))
                 
        for r in range(m):
            for c in range(n):

                if rooms[r][c] == 0:
                    q.append((r,c))
                    visited.add((r,c))
        dist = 0
        while q:

            for i in range(len(q)):
                n_r,n_c = q.popleft()
                rooms[n_r][n_c] = dist

                add_to_q(n_r-1,n_c)
                add_to_q(n_r+1,n_c)
                add_to_q(n_r,n_c-1)
                add_to_q(n_r,n_c+1)
        
            dist += 1