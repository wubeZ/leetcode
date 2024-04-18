class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        direction = [[1,0],[0,1],[-1,0],[0,-1]]
        inbound = lambda x, y : 0<= x < len(grid) and 0 <= y < len(grid[0])
        count = [0]
        visited = set()
        
        
        def solve(i, j):
            
            for x, y in direction:
                ni, nj = i + x, j + y
                if (ni, nj) in visited:
                    continue
                if not inbound(ni, nj) or grid[ni][nj] == 0:
                    count[0] += 1
                    continue
                
                visited.add((ni,nj))
                solve(ni, nj)
        
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) not in visited and grid[i][j] == 1:
                    visited.add((i, j))
                    solve(i, j)
                    
        
        return count[0]