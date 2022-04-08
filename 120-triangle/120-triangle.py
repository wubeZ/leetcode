class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        memo = {}
        def dp(i,j):
            if i == len(triangle)-1:
                return triangle[i][j]
            
            if (i,j) in memo:
                return memo[(i,j)]
            
            memo[(i,j)] = min(dp(i+1,j),dp(i+1,j+1)) + triangle[i][j]
            
            return memo[(i,j)]
        
        return dp(0,0)