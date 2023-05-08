class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        
        total = 0
        for i in range(len(mat)):
            total += mat[i][i]
            total += mat[len(mat)-i-1][i]
        
        return total - mat[len(mat)//2][len(mat)//2] if len(mat)%2 != 0 else total