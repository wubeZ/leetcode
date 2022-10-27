class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0: return 0
        @lru_cache(None)
        def dfs(i, amount):
            if i >= len(coins) or amount < 0:
                return float("inf")
            
            if amount == 0:
                return 0
            
            ans = min(dfs(i, amount - coins[i]) + 1, dfs(i+1, amount))
            return ans
        
        val = dfs(0, amount)
        
        return val if val != float("inf") else -1
        