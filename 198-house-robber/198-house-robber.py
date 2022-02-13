class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        left = nums[0]
        result = max(nums[0], nums[1])
        
        for i in range(2, len(nums)):
            left ,result = result, max(result, left + nums[i])
            
        return result