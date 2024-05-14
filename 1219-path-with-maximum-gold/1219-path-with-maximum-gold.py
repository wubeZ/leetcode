class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        direction = [[-1,0],[1,0],[0,1],[0,-1]]
        in_bound = lambda x, y: 0 <= x < len(grid) and 0 <= y < len(grid[0])
        res = [0]
        
        def dfs(i, j, seen, count):
            
            for dx, dy in direction:
                ni, nj = i + dx, j + dy
                
                if in_bound(ni, nj) and (ni, nj) not in seen and grid[ni][nj] != 0:
                    seen.add((ni, nj))
                    count += grid[ni][nj]
                    dfs(ni, nj, seen, count)
                    seen.remove((ni, nj))
                    count -= grid[ni][nj]
            
            res[0] = max(res[0], count)
            return 
    
    
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != 0:
                    count = grid[i][j]
                    seen = set()
                    seen.add((i, j))
                    dfs(i, j, seen, count)
                    
        
        return res[0]
                    
            