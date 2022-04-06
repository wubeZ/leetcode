class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        heap = []
        heapq.heappush(heap, (grid[0][0], 0, 0))
        neighbors = [[-1,0],[1,0],[0,-1],[0,1]]
        in_bound = lambda row,col : 0<= row< len(grid) and 0 <= col < len(grid[0])
        visited = set()
        
        while heap:
            currentMax, row, col = heapq.heappop(heap)
            if row == len(grid)-1 and col == len(grid[0])-1:
                return currentMax
            if (row, col) in visited:
                continue
            visited.add((row, col))
            for i, j in neighbors:
                newRow, newCol = row + i, col + j
                if (newRow, newCol) not in visited and in_bound(newRow, newCol):
                    heapq.heappush(heap, (max(currentMax, grid[newRow][newCol]), newRow, newCol))
        
        return -1