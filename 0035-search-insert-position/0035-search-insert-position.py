class Solution:
    def searchLeft(self, nums, target):
        left = -1
        right = len(nums)
        
        while left + 1 < right:
            
            mid = left + (right - left) // 2
            
            if nums[mid] < target:
                left = mid
            else:
                right = mid
                
        return right
        
        
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        return self.searchLeft(nums, target)
            