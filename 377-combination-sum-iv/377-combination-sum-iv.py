class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1)
        
        dp[0] = 1
        for i in range(target + 1):
            for val in nums:
                if val + i <= target:
                    dp[i+val] += dp[i]
        
        
        return dp[-1]