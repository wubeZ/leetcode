class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        direction = [[1,0],[0,1],[-1,0],[0,-1]]
        inbound = lambda x, y: 0 <= x < len(grid) and 0 <= y < len(grid[0])
        
        def solve(i, j):
            
            for x,y in direction:
                ni, nj = i + x, j + y
                
                if inbound(ni, nj) and grid[ni][nj] == "1" and (ni, nj) not in visited:
                    visited.add((ni, nj))
                    solve(ni, nj)
        
        visited = set()
        count = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and (i, j) not in visited:
                    count += 1
                    visited.add((i, j))
                    solve(i, j)
        
        
        return count
                    