class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = [1] * len(nums)
        ans = -1
        for i in range(len(nums)-1,-1,-1):
            j = i + 1
            temp = 0
            while j < len(nums):
                if nums[i] < nums[j]:
                    temp = max(memo[j], temp)
                j += 1
            memo[i] += temp
            
            ans = max(ans, memo[i])
        
        
        return ans