class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = [ [0] * len(grid[0]) for i in range(len(grid))]
        
        dp[0][0] = grid[0][0]
        
        for j in range(1,len(grid[0])):
            dp[0][j] = dp[0][j-1] + grid[0][j]
        for j in range(1,len(grid)):
            dp[j][0] = dp[j-1][0] + grid[j][0]
        
        for i in range(1,len(grid)):
            for j in range(1, len(grid[i])):
                dp[i][j] = min(dp[i-1][j],dp[i][j-1]) + grid[i][j]
        
        return dp[len(grid)-1][len(grid[0])-1]