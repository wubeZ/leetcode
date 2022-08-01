class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        in_bound = lambda x,y : 0 <= x < m  and 0 <= y < n
        memo = {}
        def dp(r, c):
            if in_bound(r, c):
                if (r, c) in memo:
                    return memo[(r, c)]
                if (r,c) == (m-1,n-1):
                    return 1    
                memo[(r, c)] = dp(r + 1, c) + dp(r, c + 1)
                return memo[(r, c)]
            
            else: return 0
            
        return dp(0, 0)
        
        
        
        
        
        
        
        
        
        
        