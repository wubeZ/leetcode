class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            res ^= nums[i]
            res ^= i
        
        res ^= len(nums)
        
        return res 