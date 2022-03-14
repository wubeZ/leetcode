class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        direction = [[1,0],[0,1],[-1,0],[0,-1]]
        visited = set()
        n = len(grid)
        m = len(grid[0])
        count = 0
        in_bound = lambda row,col : 0 <= row < n and 0 <= col < m
        
        def dfs(row,col):
            
            for dir in direction:
                newrow ,newcol = row + dir[0] , col + dir[1]
                
                if (newrow ,newcol) not in visited and in_bound(newrow,newcol) \
                and grid[newrow][newcol] == 1:
                    visited.add((newrow,newcol))
                    dfs(newrow,newcol)
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i in (0 , n - 1) or j in (0 , m - 1)) and \
                (i,j) not in visited and grid[i][j] == 1:
                           visited.add((i,j))
                           dfs(i,j)
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i,j) not in visited and grid[i][j] == 1:
                           count += 1
        
                           
        return count
                           