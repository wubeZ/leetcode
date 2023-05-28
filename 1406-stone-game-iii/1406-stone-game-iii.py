class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        
        @lru_cache(None)
        def dfs(idx):
            if idx >= len(stoneValue):
                return 0
            
            ans = float("-inf")
            one, two, three = float("-inf"), float("-inf"), float("-inf")
            
            one = stoneValue[idx] - dfs(idx + 1)
            if idx + 1 < len(stoneValue):
                two = stoneValue[idx] + stoneValue[idx + 1] - dfs(idx + 2)
            if idx + 2 < len(stoneValue):
                three = stoneValue[idx] + stoneValue[idx + 1] + stoneValue[idx + 2] - dfs(idx + 3)
            
            ans = max(ans, one, two , three)
            return ans
        
        
        val = dfs(0)
        
        
        if val == 0:
            return "Tie"
        
        if val < 0:
            return "Bob"
        
        return "Alice"