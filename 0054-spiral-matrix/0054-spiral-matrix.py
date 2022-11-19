class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        maxrow, maxcol = len(matrix), len(matrix[0])
        n = len(matrix)*len(matrix[0])
        minrow, mincol = 0, 0
        ans = []
        c = 0
        while minrow < maxrow and mincol < maxcol:
            row, col = minrow, mincol
            for k in range(col, maxcol):
                ans.append(matrix[row][k])
                
            row += 1
            for j in range(row, maxrow):
                ans.append(matrix[j][maxcol-1])
                
            col = maxcol - 2
            for l in range(col, mincol,-1):
                ans.append(matrix[maxrow-1][l])
            
            row = maxrow - 1
            for m in range(row, minrow,-1):
                ans.append(matrix[m][mincol])
                
            maxrow -= 1
            maxcol -= 1
            minrow += 1
            mincol += 1
            
        return ans[:n]