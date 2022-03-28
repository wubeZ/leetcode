class Solution:
    def findPivot(self,nums):
        left, right = 0, len(nums) - 1
        
        if nums[right] > nums[left]:
            return right + 1
        
        while left <= right:
            mid = left + (right - left)//2
            if nums[mid] >= nums[0]:
                left = mid + 1
            else:
                right = mid - 1
        return left
        
    def search(self, nums: List[int], target: int) -> int:       
        def binarySearch(left,right):
            while left <= right:
                mid = left + (right - left)//2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1
        
        best = self.findPivot(nums)
        if nums[0] > target:
            return binarySearch(best, len(nums)-1)
        return binarySearch(0, best-1) 
        
    
            