'''
Rotate each corner of a square 
use left, right, top, down pointers
'''
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        l, r = 0, len(matrix)-1

        while l<r:
            top, bottom = l, r
            for i in range(r-l):

                #saving top left in a temp
                topLeft = matrix[top][l+i]

                #saving bottom left to top left
                matrix[top][l+i] = matrix[bottom-i][l]

                #bottom right to bottom left
                matrix[bottom-i][l] = matrix[bottom][r-i]

                #top right to bottom right
                matrix[bottom][r-i] = matrix[top+i][r]

                #temp top left to top right
                matrix[top+i][r] = topLeft
            r -= 1
            l += 1
        return matrix