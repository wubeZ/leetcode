class Solution:
    
    def binsearch(self, l, r, nums, target):
        while l <= r:
            mid = l + (r - l)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return -1

    def search(self, nums: List[int], target: int) -> int:
        left, right = 0 , len(nums)-1
        while left < right:
            if nums[left] < nums[right]:
                break
            mid = left + (right - left)//2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        
        leftsearch =  self.binsearch(left, len(nums)-1, nums, target)
        rightsearch = self.binsearch(0, left-1, nums, target)
        
        if leftsearch == -1 and rightsearch == -1:
            return -1
        if leftsearch == -1:
            return rightsearch
        return leftsearch
        
        
        
        