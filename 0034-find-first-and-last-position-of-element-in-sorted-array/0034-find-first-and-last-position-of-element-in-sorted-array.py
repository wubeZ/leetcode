class Solution:
    
    def search(self, nums, target, turn):
        left = -1
        right = len(nums)
        
        while left + 1 < right:
            mid = left + (right - left)//2
            
            if nums[mid] < target:
                left = mid
            elif nums[mid] == target:
                if turn:
                    right = mid
                else:
                    left = mid
            else:
                right = mid
        
        if turn:
            return right if right != len(nums) and nums[right] == target else -1
        
        return left if nums[left] == target else -1
        
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1,-1]
        left = self.search(nums, target, True)
        right = self.search(nums, target, False)
        
        return [left, right]