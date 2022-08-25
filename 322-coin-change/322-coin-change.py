class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0: return 0
        
        memo = {0:0}
        
        def dfs(num):
            if num in memo:
                return memo[num]
            
            res = float("inf")
            for i in range(len(coins)):
                if num - coins[i] >= 0:
                    res = min(res, dfs(num - coins[i]) + 1)
            memo[num] = res 
            return memo[num]
            
        
        dfs(amount)
        
        return memo[amount] if memo[amount] != float("inf") else -1