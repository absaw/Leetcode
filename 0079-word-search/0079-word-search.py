class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        m = len(board)
        n = len(board[0])
        
        path = set()
        neighbors = [[1,0],[-1,0],[0,1],[0,-1]]
        def dfs(r,c,ptr):
            if ptr == len(word):
                return True
            if (r not in range(m) or
                c not in range(n) or
                board[r][c] != word[ptr] or
                (r,c) in path):
                return False
            
            path.add((r,c))
            found = False
            for n_r,n_c in neighbors:
                
                found = found or dfs(r+n_r,c+n_c,ptr+1)
                if found:
                    break
            path.remove((r,c))
            return found
        
        for r in range(m):
            for c in range(n):
                ch = board[r][c]
                if dfs(r,c,0):
                    return True
        return False