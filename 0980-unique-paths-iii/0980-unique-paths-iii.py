class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        directions = [[-1,0],[0,-1],[1,0],[0,1]]
        inbound = lambda x,y: 0 <= x < len(grid) and 0 <= y < len(grid[0])
        seen = set()
        self.ans = 0
        total = len(grid[0])*len(grid)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == -1:
                    total -= 1
                elif grid[i][j] == 1:
                    start = (i,j)
        
        def dfs(r,c):
            if len(seen) == total:
                if grid[r][c] == 2:
                    self.ans += 1
                return 
            
            if grid[r][c] == 2:
                return
            
            for x, y in directions:
                nr,nc = r+x, c+y
                if inbound(nr,nc) and grid[nr][nc] != -1 and (nr,nc) not in seen:
                    seen.add((nr,nc))
                    dfs(nr,nc)
                    seen.remove((nr,nc))
        seen.add(start)                    
        dfs(start[0], start[1])
        return self.ans