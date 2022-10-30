class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        def inbound(newrow, newcol):
            return 0 <= newrow < m and 0 <= newcol < n
        
        queue = deque()
        seen = {(0,0):0}
        steps = 0
        queue.append([0,0,0])
        while queue:
            length = len(queue)
            for _ in range(length):
                row, col, obs = queue.popleft()
                if obs > k:
                    continue

                if (row,col) == (m-1,n-1):
                    return steps

                for dx, dy in directions:
                    newrow, newcol = row + dx, col + dy
                    if inbound(newrow,newcol):
                        nobs = obs
                        if grid[newrow][newcol] == 1:
                            nobs += 1
                        if nobs < seen.get((newrow,newcol), float("inf")):
                            seen[(newrow, newcol)] = nobs
                            queue.append([newrow,newcol,nobs])
            steps +=  1

        return -1
        