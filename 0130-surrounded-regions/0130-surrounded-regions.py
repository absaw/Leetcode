class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        M = len(board)
        N = len(board[0])
        ignore = set()
        def dfs(r,c):
            if (r not in range(M) or 
                c not in range(N) or 
                board[r][c] =="X" or 
                (r,c) in ignore):
                return
            # board[r][c] = "X"
            ignore.add((r,c))
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
        for r in range(M):
            if board[r][0] == "O":
                dfs(r,0)
            if board[r][N-1]=="O":
                dfs(r,N-1)
        for c in range(N):
            if board[0][c]=="O":
                dfs(0,c)
            if board[M-1][c] == "O":
                dfs(M-1,c)
        for r in range(M):
            for c in range(N):
                if (r,c) not in ignore and board[r][c] == "O":
                    board[r][c] = "X"

        return board