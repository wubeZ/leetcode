class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        left, right = 0, len(nums)-1
        
        while left <= right:
            if nums[left] != val:
                count += 1
                left += 1
            elif nums[left] == val:
                nums[left], nums[right] = nums[right], nums[left]
                right -= 1
            
        return count