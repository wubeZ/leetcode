class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {1:1, 2:2}
        def solve(i):
            if i in memo:
                return memo[i]
            
            memo[i] = solve(i-1) + solve(i-2) 
            return memo[i]
        
        return solve(n)