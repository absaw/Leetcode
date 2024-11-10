class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        #find zeros
        zeroRows = set()
        zeroCols = set()
        m = len(matrix)
        n = len(matrix[0])
        for r in range(m):
            for c in range(n):
                if matrix[r][c]==0:
                    zeroRows.add(r)
                    zeroCols.add(c)
        #setting all cols in rows to zero
        while zeroRows:
            currRow = zeroRows.pop()
            for c in range(n):
                matrix[currRow][c]=0
        while zeroCols:
            currCol = zeroCols.pop()
            for r in range(m):
                matrix[r][currCol] = 0

        return matrix