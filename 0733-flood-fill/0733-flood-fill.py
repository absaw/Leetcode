class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        path = set()
        m = len(image)
        n = len(image[0])
        startColor = image[sr][sc]

        if color == startColor:
            return image
        
        def dfs(row, col):
            
            if (row not in range(m) or
                col not in range(n) or 
                (row,col) in path or 
                image[row][col] != startColor):
                return
            
            image[row][col] = color
            path.add((row,col))
            dfs(row+1,col)
            dfs(row-1,col)
            dfs(row,col+1)
            dfs(row,col-1)
        dfs(sr,sc)
        return image