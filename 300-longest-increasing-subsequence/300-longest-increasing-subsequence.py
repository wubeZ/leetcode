class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        dp = [1] * len(nums)
        
        for i in range(len(nums)):
            j = i+1
            while j < len(nums):
                if nums[i] < nums[j]:
                    dp[j] = max(dp[j], dp[i] + 1)
                j += 1
            
        return max(dp)
        