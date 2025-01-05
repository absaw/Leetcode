class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rowDict={i:set() for i in range(9)}
        colDict={i:set() for i in range(9)}
        boxDict={}

        for r in range(3):
            for c in range(3):
                boxDict[(r,c)] = set()
            
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    continue
                if val in rowDict[r]:
                    return False
                rowDict[r].add(val)

                if val in colDict[c]:
                    return False
                colDict[c].add(val)

                if val in boxDict[(r//3,c//3)]:
                    return False
                boxDict[(r//3,c//3)].add(val)

        return True