class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        queue = deque()
        queue.append((0,0,1))
        direction = [[1,0],[0,1],[-1,0],[0,-1],[1,1],[1,-1],[-1,1],[-1,-1]]
        in_bound = lambda x,y : 0 <= x < n and 0 <= y < m
        
        while queue:
            row, col , count = queue.popleft()
            if grid[row][col] == 0:
                if (row, col) == (n-1, m-1):
                    return count
                
                grid[row][col] = 1
                
                for i, j in direction:
                    newrow, newcol = row + i, col + j

                    if in_bound(newrow, newcol) and grid[newrow][newcol] == 0:
                        queue.append((newrow,newcol, count + 1))

        return -1