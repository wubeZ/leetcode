class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0]* (len(cost))
        i = 0
        while i < len(cost):
            if i < 2:
                dp[i] = cost[i]
            else:
                dp[i] = min(dp[i-1], dp[i-2]) + cost[i]
            i+= 1
            
        return min(dp[-1],dp[-2])

    
            
        

        
        