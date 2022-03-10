class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [[1,0],[0,1],[0,-1],[-1,0]]
        visited = set()
        m = len(grid)
        area = 0
        in_bound = lambda row,col : 0 <= row < m and 0 <= col < len(grid[row]) 

        def dfs(row, col):
            visited.add((row,col))
            count = 1
            for dir in directions:
                newrow , newcol = row + dir[0] , col + dir[1]
                
                if (newrow, newcol) in visited or not in_bound(newrow, newcol) \
                or grid[newrow][newcol] != 1:
                    continue
                count += dfs(newrow, newcol)
        
            return count
        
        for i in range(m):
            for j in range(len(grid[i])):
                if (i, j) not in visited and in_bound(i, j) and grid[i][j] == 1:
                    area = max(area, dfs(i, j))
        
        return area
        
        
                
                