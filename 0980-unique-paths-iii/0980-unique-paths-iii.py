class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        directions = [[-1,0],[0,-1],[1,0],[0,1]]
        n, m = len(grid), len(grid[0])
        inbound = lambda x,y: 0 <= x < n and 0 <= y < m
        self.ans = 0
        total = (1 << n*m) - 1
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == -1:
                    total ^= 1 << ((i*m+j))
                elif grid[i][j] == 1:
                    start = (i,j)
        
        def dfs(r,c, mask):
            if mask == total:
                if grid[r][c] == 2:
                    self.ans += 1
                return 
            if grid[r][c] == 2:
                return
            
            for x, y in directions:
                nr,nc = r+x, c+y
                if inbound(nr,nc) and grid[nr][nc] != -1 and mask & (1 << (nr*m + nc))== 0:
                    dfs(nr,nc, mask | (1 << (nr*m + nc)))
                                        
        dfs(start[0], start[1], 1 << (start[0]*m +start[1]))
        return self.ans