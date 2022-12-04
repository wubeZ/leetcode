class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        memo = {}
        
        def dfs(l, r):
            if l == r:
                return nums[l]
            if (l,r) in memo:
                return memo[(l,r)]
            
            left = nums[l] - dfs(l + 1, r)
            right = nums[r] - dfs(l , r -1)
            
            memo[(l,r)] = max(left, right)
            
            return memo[(l,r)]
            
            
        return dfs(0, len(nums)-1) >= 0