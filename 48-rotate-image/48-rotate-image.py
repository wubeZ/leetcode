class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        left, right = 0, len(matrix)-1
        while left < right:
            for j in range(len(matrix[0])):
                matrix[left][j], matrix[right][j] = matrix[right][j], matrix[left][j]
            left += 1
            right -= 1
            
        for i in range(len(matrix)):
            for j in range(i, len(matrix[0])):
                if i != j:
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
