class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        @cache
        def dfs(bought, idx):
            if idx == len(prices):
                if bought:
                    return float("-inf")
                return 0
            profit = 0
            if bought:
                profit = max(dfs(bought,idx+1), prices[idx] + dfs(not bought, idx+1))
                return profit
            profit = max(dfs(bought, idx+1), -prices[idx] + dfs(not bought, idx+1))
            return profit
        
        return dfs(False, 0)