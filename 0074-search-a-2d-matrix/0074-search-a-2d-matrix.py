class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        top = 0 
        bottom = m-1
        midRow = 0
        while top<= bottom:
            midRow = (top+bottom) // 2

            if target<matrix[midRow][0]:
                bottom = midRow - 1
            elif target > matrix[midRow][-1]:
                top = midRow + 1
            else:
                break
        
        if top>bottom:
            return False

        l , r = 0, n-1

        while l <= r:
            mid = (l + r) // 2

            if matrix[midRow][mid] == target:
                return True
            elif target<matrix[midRow][mid]:
                r = mid -1
            else:
                l = mid+1
        return False
