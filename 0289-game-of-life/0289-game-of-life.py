class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        def getCount(r,c):
            neighbors = [[1,0],
                        [-1,0],
                        [1,1],
                        [-1,-1],
                        [0,1],
                        [0,-1],
                        [1,-1],
                        [-1,1]
                        ]
            count = 0
            for add_r, add_c in neighbors:
                new_r = add_r + r
                new_c = add_c + c
                
                if (new_r in range(m) and 
                    new_c in range(n) and 
                    board[new_r][new_c] in [1,3]):
                    count+=1
            return count

        for r in range(m):
            for c in range(n):
                count = getCount(r,c)
                if board[r][c] == 0 and count == 3:
                    board[r][c] =2
                elif board[r][c]==1:
                    if count in range(2,4):
                        board[r][c] = 3
                    else:
                        board[r][c] = 1
        n_map = {0:0,1:0,2:1,3:1}
        for r in range(m):
            for c in range(n):
                board[r][c] = n_map[board[r][c]]
        