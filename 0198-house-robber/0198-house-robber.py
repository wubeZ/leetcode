class Solution:
    def rob(self, nums: List[int]) -> int:
        @lru_cache(None)
        def dfs(i):
            if i >= len(nums):
                return 0
            
            profit = max(dfs(i+1), dfs(i+2) + nums[i])
            
            return profit
        
        return dfs(0)
        