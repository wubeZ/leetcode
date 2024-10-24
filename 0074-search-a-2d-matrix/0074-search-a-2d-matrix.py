class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        l, r = -1, len(matrix)
        
        while l + 1 < r:
            mid = l + (r - l)//2
            
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] > target:
                r = mid
            else:
                l = mid
        
        
        row = l
        
        l, r = -1, len(matrix[0])
        
        while l + 1 < r:
            mid = l + (r - l)//2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                l = mid
            else:
                r = mid
        
        
        
        return False
        