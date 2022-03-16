class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        count = 0
        self.best = -1
        def finder(grid, i):
            left , right = 0 , len(grid[i])-1
            while left <= right :
                mid = left + (right - left)//2
                if grid[i][mid] >= 0:
                    left = mid + 1
                elif grid[i][mid] < 0:
                    self.best = mid
                    right = mid - 1
            return self.best
        
        for row in range(n):
            first = finder(grid, row)
            if first != -1:
                count += (m - first) 
        
        return count
        
        
