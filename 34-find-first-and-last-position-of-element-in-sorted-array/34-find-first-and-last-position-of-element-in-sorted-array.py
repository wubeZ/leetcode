class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        self.ans = -1
        def finder(nums, target, check):
            left, right = 0, len(nums) - 1
            
            while left <= right:
                mid = left + (right - left)//2
                if nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    self.ans = mid
                    if check:
                        right = mid - 1
                    else:
                        left = mid + 1
                        
            return self.ans
        
        first = finder(nums, target, True)
        
        if first == -1:
            return [-1,-1]
        else:
            return[first , finder(nums, target, False)]