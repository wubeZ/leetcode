class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        @lru_cache(maxsize=None)
        def solve(day, canBuy):
            if day >= len(prices):
                return 0
            
            buyOnDay = 0
            sellOnDay = 0
            
            if canBuy:
                buyOnDay = -prices[day] + solve(day + 1, False)
            else:
                sellOnDay = prices[day] + solve(day + 2, True)
                
            doNothing = solve(day + 1, canBuy)
            maxProfit = max(buyOnDay, sellOnDay, doNothing)
            
            return maxProfit
        
        return solve(0, True)