class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        
        def dp(N):
            if N < 0:
                return 0
            elif N < 2:
                return 1
                
            if N in memo:
                return memo[N]
            
            memo[N] = dp(N-1) + dp(N-2)
            return memo[N]
        
        return dp(n)