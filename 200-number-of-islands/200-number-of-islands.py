class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        in_bound = lambda x,y : 0 <= x < len(grid) and 0 <=  y < len(grid[0])
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        visited = set()
        
        def dfs(r,c):
            visited.add((r, c))
            for dx ,dy in directions:
                nr, nc = r + dx, c + dy
                if in_bound(nr,nc) and grid[nr][nc] == "1" and (nr,nc) not in visited:
                    dfs(nr, nc)
        
            return 
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and (i,j) not in visited:
                    ans += 1
                    dfs(i,j)
        
        return ans