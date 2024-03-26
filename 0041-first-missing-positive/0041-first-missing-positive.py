class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        start = 1
        end = len(nums) + 1
        
        i = 0
        while i < len(nums):
            if nums[i] < start or nums[i] > end:
                nums[i] = -2
                i += 1
                continue
            pos = nums[i] - 1
            if pos < len(nums) and nums[pos] == nums[i]:
                i += 1
                continue
            if pos < len(nums) and i != pos:
                nums[i], nums[pos] = nums[pos], nums[i]
            else:
                i += 1
        
        
        for i in range(len(nums)):
            if nums[i] == -2 or nums[i] != i + 1:
                return i + 1
        
        return end