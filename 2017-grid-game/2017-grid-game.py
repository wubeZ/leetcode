class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        
        left = 0
        right = sum(grid[0])
        
        ans = float("inf")
        
        for i in range(n):
            right -= grid[0][i]
            
            possible = max(left, right)
            ans = min(ans, possible)
            
            left += grid[1][i]
        
        
        return ans