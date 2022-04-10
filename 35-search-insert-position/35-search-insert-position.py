class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        best = -1
        while left <= right :
            mid = left + (right - left)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                best = mid
                right = mid - 1
            else:
                left = mid + 1
        
        if best == -1:
            return len(nums)
        return best