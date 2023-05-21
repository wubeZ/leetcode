class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        directions = [[-1,0],[0,-1],[1,0],[0,1]]
        
        inbound = lambda x,y : 0 <= x < len(grid) and 0 <= y < len(grid[0])
        
        start = set()
        first_island = set()
        
        def get_boundary(i, j):
            first_island.add((i,j))
            for di, dj in directions:
                x, y = i + di, j + dj
                if inbound(x,y):
                    if (x,y) not in first_island and grid[x][y] == 1:
                        get_boundary(x, y)
                    if grid[x][y] == 0:
                        start.add((0, i, j))
                        
        def find_first_land():
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == 1:
                        return i, j
                    
        start_i, start_j = find_first_land()
        
        get_boundary(start_i, start_j)
        
        seen = set()
        
        queue = list(start)
        for step, i, j in queue:
            for di, dj in directions:
                x, y = i + di, j + dj
                if inbound(x,y) and (x,y) not in seen:
                    if grid[x][y] == 1 and (x,y) not in first_island:
                        return step
                    
                    elif grid[x][y] == 0:
                        seen.add((x,y))
                        queue.append((step + 1, x, y))