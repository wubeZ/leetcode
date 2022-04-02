class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        queue = deque([])
        visited = set()
        in_bound = lambda row,col: 0<= row < len(grid) and 0 <= col < len(grid[0])
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    visited.add((i,j))
                    queue.append((i,j))
    
        if len(queue) == 0 or len(queue) == len(grid)*len(grid[0]):
            return -1
        
        maxDistance = -1        
        
        while queue:
            maxDistance += 1
            n = len(queue)
            i = 0
            while i < n:
                cur = queue.popleft()
                for dir in directions:
                    row, col = cur[0]+dir[0], cur[1]+dir[1]
                    if (row,col) not in visited and in_bound(row,col):
                        queue.append((row,col))
                        visited.add((row,col))        
                i += 1
            
        return maxDistance