class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        count = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] < 0:
                    count += (m - j)
                    break
                    
        return count