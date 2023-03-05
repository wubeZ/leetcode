class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        prefix = [0]
        n = len(grid[0])
        suffix = [0]
        
        for i in range(n):
            prefix.append(prefix[-1] + grid[0][i])
        
        for j in range(n-1,-1,-1):
            suffix.append(suffix[-1] + grid[1][j])
        
        prefix = prefix[1:]
        suffix = suffix[::-1]
        suffix.pop()
        
        ans = float("inf")
        
        for i in range(n):
            left = prefix[-1] - prefix[i]
            right = suffix[0] - suffix[i]
            
            possible = max(left, right)
            ans = min(ans , possible)
        
        return ans