class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        direction = [[0,1],[1,0],[-1,0],[0,-1]]
        in_bound = lambda x, y: 0 <= x < len(grid) and 0 <= y < len(grid[0])
        
        def dfs(r, c):
        
            for i, j in direction:
                nr, nc = r + i, c + j
                if not in_bound(nr,nc) or grid[nr][nc] == 0:
                    self.count += 1
                if in_bound(nr,nc) and (nr, nc) not in visited and grid[nr][nc] == 1:
                    visited.add((nr,nc))
                    dfs(nr, nc)
        
        
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    self.count = 0
                    visited = {(i,j)}
                    dfs(i,j)
                    return self.count
        
        
        