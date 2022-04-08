class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}
        def dp(i):
            if i < 2:
                return cost[i]
            
            if i in memo:
                return memo[i]
            
            memo[i] = min(dp(i-1), dp(i-2)) + cost[i]
            return memo[i]
        
        return min(dp(len(cost)-1), dp(len(cost)-2))