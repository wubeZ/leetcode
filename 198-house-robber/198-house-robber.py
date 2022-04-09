class Solution:
    def rob(self, nums: List[int]) -> int:
        @cache    
        def dp(i):
            if i >= len(nums):
                return 0
            return max(nums[i] + dp(i+2) , dp(i+1))
        
        return dp(0)