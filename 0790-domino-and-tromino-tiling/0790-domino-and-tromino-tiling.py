class Solution:
    def numTilings(self, n: int) -> int:
        dp = {}
        
        def solve(n):
            if n in dp:
                return dp[n]
            if n < 0 or n == 0.5:
                return 0
            if n == 0 or n == 1.5:
                return 1
            if round(n) == n:
                dp[n] = solve(n - 1) + solve(n - 2) + 2* solve(n - 1.5)
            else:
                dp[n] = solve(n - 1) + solve(n - 1.5)
                
            dp[n] = dp[n]%(10**9+7)
            
            return dp[n]

        return solve(n)