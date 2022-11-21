class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = float("-inf")
        l = 0
        prefix = 0
        for r in range(len(nums)):
            prefix += nums[r]
            ans = max(ans, prefix)    
            if prefix < 0:
                prefix = 0
        
        return ans