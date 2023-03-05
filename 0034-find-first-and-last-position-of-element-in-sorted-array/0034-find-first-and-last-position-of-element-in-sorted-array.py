class Solution:
    
    def searchLeft(self, nums, target):
        left = -1
        right = len(nums)
        
        while left + 1 < right:
            
            mid = left + (right - left)//2
            
            if nums[mid] < target:
                left = mid
            else:
                right = mid
        
        return right if right != len(nums) and nums[right] == target else -1
        
        
        
        
    def searchRight(self, nums, target):
        left = -1
        right = len(nums)
        
        while left + 1 < right:
            
            mid = left + (right - left)//2
            
            if nums[mid] <= target:
                left = mid
            else:
                right = mid
        
        return left if nums[left] == target else -1
        
    
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1,-1]
        left = self.searchLeft(nums, target)
        right = self.searchRight(nums, target)
        
        return [left, right]
        
        
        
        
        
        
    
        
            
            