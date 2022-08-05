class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        memo = {}
        
        def dfs(i, total):
            
            if i > len(nums)-1 or total > target:
                return 0
            
            if target == total: return 1
            
            if (i, total) in memo: return memo[(i, total)]
            
            memo[(i, total)] = dfs(i+1, total) + dfs(0, total + nums[i])
            
            return memo[(i, total)]
        
        
        return dfs(0,0)
  