class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        directions = [[-1,0],[0,-1],[1,0],[0,1]]
        inbound = lambda x,y: 0 <= x < len(grid) and 0 <= y < len(grid[0])
        count = 0
        self.ans = 0
        nums = {}
        total = (1 << len(grid[0])*len(grid)) - 1
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                nums[(i,j)] = count
                count += 1
                if grid[i][j] == -1:
                    total ^= 1 << nums[(i,j)] 
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
                if inbound(nr,nc) and grid[nr][nc] != -1 and (mask & (1 << nums[(nr,nc)]))== 0:
                    dfs(nr,nc, mask | (1<< nums[(nr,nc)]))
                                        
        dfs(start[0], start[1], 1 << nums[start])
        return self.ans