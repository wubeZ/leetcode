class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) <= 3: return max(nums)
        
        def get(nums):
            dp = [0] * len(nums)
            if len(dp) == 1: return nums[0]

            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])

            for i in range(2,len(nums)):
                dp[i] = max( dp[i-1] , dp[i-2] + nums[i] ) 

            return dp[-1]
        
        return max(get(nums[1:]), get(nums[:-1]))