class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        m = len(mat)
        n = len(mat[0])
        queue = deque()
        for r in range(m):
            for c in range(n):
                if mat[r][c]==0:
                    queue.append((r,c))
                else:
                    mat[r][c] = float('inf')
        neighbors = [[0,1],[0,-1],[1,0],[-1,0]]
        while queue:
            row, col = queue.popleft()
            
            #traverse through neighbors and update the neighbors
            for add_r, add_c in neighbors:
                n_r,n_c = row+add_r, col+add_c
                
                if n_r in range(m) and \
                    n_c in range(n) and \
                    mat[n_r][n_c] > (1+mat[row][col]):
                    queue.append((n_r,n_c))
                    mat[n_r][n_c] = (1+mat[row][col])
        return mat