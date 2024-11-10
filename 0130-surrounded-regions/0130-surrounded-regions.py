"""
Think of it as a reverse problem
instead of 
capturing the surrounded region
I want to 
caputure everything except the un-surrounded region.Confusing right. look at the O at (3,1). That is unsurrounded cause its on the border. So i first mark(T)all the unsurrounded. Then I convert the surrounded Os to Xs. Then I unmark the Ts, back to Os
1. dfs to capture unsurrounded regions
2. 
"""

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        def dfs(r,c):
            if (r not in range(m) or 
                c not in range(n) or
                board[r][c] !='O'):
                return
            board[r][c] = 'T'
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
        for r in range(m):
            for c in range(n):
                if (r==0 or r==(m-1)):
                    dfs(r,c)
                elif(c==0 or c==(n-1)):
                    dfs(r,c)
        
        for r in range(m):
            for c in range(n):
                if board[r][c] =='O':
                    board[r][c]='X'
                elif board[r][c] =='T':
                    board[r][c] = 'O'
        return board