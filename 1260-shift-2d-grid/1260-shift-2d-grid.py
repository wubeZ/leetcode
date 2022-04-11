class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        k = k %(len(grid) * len(grid[0]))
        count = len(grid)*len(grid[0]) - k
        ans = [[0]*len(grid[0]) for i in range(len(grid))]
        temp, temp2 = deque(), deque()
        
        if k == 0:
            return grid
        
        for i in range(len(grid)-1,-1,-1):
            for j in range(len(grid[0])-1,-1,-1):
                if k > 0:
                    temp.append(grid[i][j])
                    k -= 1
                else:
                    break
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if count > 0:
                    temp2.append(grid[i][j])
                    count -= 1
                else:
                    break
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if len(temp) > 0:
                    ans[i][j] = temp.pop()
                elif len(temp2) > 0:
                    ans[i][j] = temp2.popleft()
        
        return ans