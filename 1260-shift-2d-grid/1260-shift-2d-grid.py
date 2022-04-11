class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m,n = len(grid), len(grid[0])
        k = k % (m*n)
        if k == 0:
            return grid
        
        temp = [grid[i][j] for i in range(m) for j in range(n)]
        temp = temp[-k:] + temp[:-k]
        temp = deque(temp)
        result = [[0]*n for i in range(m)]
        
        for i in range(m):
            for j in range(n):
                result[i][j] = temp.popleft()
                
        return result