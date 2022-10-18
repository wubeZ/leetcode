class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0]*n for i in range(n)]
        startRow, startCol, endRow, endCol = 0, 0, n ,n
        i = 0
        while startRow < endRow and startCol < endCol:
            for c in range(startCol, endCol):
                i += 1
                res[startRow][c] = i   
            startRow += 1
            for r in range(startRow, endRow):
                i += 1
                res[r][endCol-1] = i  
            endCol -= 1
            for c in range(endCol-1, startCol-1, -1):
                i += 1
                res[endRow-1][c] = i
            endRow -= 1
            for r in range(endRow-1, startRow-1, -1):
                i += 1
                res[r][startCol] = i
            startCol += 1
        
        return res
            
            
                
            
            