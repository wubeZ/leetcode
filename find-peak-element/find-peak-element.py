class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)
        
        while left + 1 < right:
            
            mid = left + (right - left)//2
            
            if nums[mid - 1] < nums[mid]:
                left = mid
            else:
                right = mid
                
        return left