class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        direction = [[0,1],[1,0],[-1,0],[0,-1]]
        in_bound = lambda x, y: 0 <= x < len(grid) and 0 <= y < len(grid[0])
        
        ans = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    count = 0
                    for dx, dy in direction:
                        nr, nc = r + dx, c + dy
                        if in_bound(nr,nc) and grid[nr][nc] == 1:
                            count += 1
                    ans += (4 - count)
        return ans
        
        